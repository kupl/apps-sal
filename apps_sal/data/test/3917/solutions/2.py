import sys
max_Int = int(1e9)

class splitFeature:
    def __init__(self, position, value):
        self.position = position
        self.value = value

def bruteForce(features, left, right):
    min_distance = max_Int
    for i in range(left, right):
        for j in range(i+1, right):
            min_distance = min(min_distance,
                               (features[i].position - features[j].position)**2 + (features[i].value - features[j].value)**2)
    return min_distance

def enhanceData(features, left, right, mid, min_distance):
    selected_population = []
    for i in range(left, right):
        if (features[i].position - features[mid].position) ** 2 <= min_distance:
            selected_population.append(features[i])
    selected_population.sort(key = lambda x: x.value)
    l = len(selected_population)
    result = max_Int
    for i in range(l):
        for j in range(i+1, l):
            if (selected_population[i].value - selected_population[j].value) ** 2 >= min_distance:
                break
            distance = (selected_population[i].position - selected_population[j].position)**2 + (selected_population[i].value - selected_population[j].value)**2
            result = min(result, distance)
    return result

def analyzeData(features, left, right):
    if right - left <= 3:
        return bruteForce(features, left, right)
    mid = (left + right) // 2
    min_distance = min(analyzeData(features, left, mid), 
                       analyzeData(features, mid+1, right))
    return min(min_distance, 
               enhanceData(features, left, right, mid, min_distance))

def main():
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    features = []
    for i in range(n):
        if (i > 0):
            A[i] += A[i-1]
        features.append(splitFeature(i , A[i]))
    sys.stdout.write(str(analyzeData(features, 0, n)))

main()

