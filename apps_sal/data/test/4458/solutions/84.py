n = int(input())
p = list(map(int, input().split()))
minp = p[0]
cnt = 0
for i in range(n):
    if p[i] <= minp: cnt += 1
    minp = min(minp, p[i])
print(cnt)
