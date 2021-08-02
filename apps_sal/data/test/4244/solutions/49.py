N = int(input())
X = input().split()

distance = 0
min_distance = float('Inf')

for i in range(1, 101):
    for j in range(N):
        distance += (int(X[j]) - i) ** 2

    min_distance = min(min_distance, distance)
    distance = 0

print(min_distance)
