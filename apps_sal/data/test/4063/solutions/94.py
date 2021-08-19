N = int(input())
d = list(map(int, input().split()))
p = [0] * N
for i in range(N):
    p[i] = (d[i], i)
p.sort()
result = abs(p[N // 2][0] - p[N // 2 - 1][0])
# print(p)
print(result)
