n, k = map(int, input().split())
ab = [int(input()) for _ in range(n)]

sab = sorted(ab)

res = 10**10

for i in range(n-k+1):
    res = min(res,sab[i+k-1]-sab[i])

print(res)
