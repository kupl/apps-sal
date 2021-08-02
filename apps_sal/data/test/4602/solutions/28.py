n, k = [int(input()) for i in range(2)]
x = list(map(int, input().split()))

distance = 0

for i in range(len(x)):
    distance += 2 * (min(x[i], abs(x[i] - k)))

print(distance)
