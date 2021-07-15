N = int(input())

p = list(map(int, input().split()))

res = 0

if p[0] == 1:
    p[0] = p[1]
    p[1] = 1
    res += 1

if p[N - 1] == N:
    p[N - 1] = p[N - 2]
    p[N - 2] = N
    res += 1


for i in range(1, N - 1):
    if p[i] == i + 1:
        p[i + 1] = i + 1
        res += 1

print(res)
