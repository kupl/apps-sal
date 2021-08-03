n, l, a = list(map(int, input().split()))
arrives = [0] * n
takes = [0] * n
for i in range(n):
    arrives[i], takes[i] = list(map(int, input().split()))

cur = 0
ans = 0
for i in range(n):
    gap = arrives[i] - cur
    ans += gap // a
    cur = arrives[i] + takes[i]

ans += (l - cur) // a
print(ans)
