(k, n) = map(int, input().split())
an = [int(num) for num in input().split()]
distance = []
for i in range(n - 1):
    distance.append(an[i + 1] - an[i])
distance.append(an[0] + (k - an[n - 1]))
distance.sort()
print(k - distance[n - 1])
