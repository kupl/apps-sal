N = int(input())
S = map(int, input().split())

Number = list(S)
Number.sort(reverse=True)
total_distance = []

for i in range(1, N):
    distance = Number[0] - Number[1]
    total_distance.append(distance)
    del Number[0]

print(sum(total_distance))
