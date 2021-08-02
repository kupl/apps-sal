h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    for _ in range(a[i]):
        ans.append(i + 1)

for i in range(h):
    if i % 2 == 0: print(*ans[i * w:(i + 1) * w])
    else: print(*reversed(ans[i * w:(i + 1) * w]))
