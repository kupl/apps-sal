n, m = map(int, input().split())
ans1 = []
ans2 = []
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        ans1.append(b)
    if b == n:
        ans2.append(a)

ans = set(ans1) & set(ans2)
if len(ans) > 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
