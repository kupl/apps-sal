N = int(input())
a = list(map(int, input().split()))
a.sort()
distance = 0
for i in range(N - 1):
    distance += a[i + 1] - a[i]
print(distance)
