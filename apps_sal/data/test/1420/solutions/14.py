(N, l) = [int(i) for i in input().strip().split()]
lights = [int(i) for i in input().strip().split()]
lights.sort()
min_d = max(lights[0], l - lights[N - 1])
for i in range(1, N):
    if min_d * 2 < lights[i] - lights[i - 1]:
        min_d = (lights[i] - lights[i - 1]) / 2
print(min_d)
