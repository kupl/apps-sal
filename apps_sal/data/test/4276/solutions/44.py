n, t = map(int, input().split())
ans = []
for i in range(n):
    a, b = map(int, input().split())
    if b <= t:
        ans.append(a)
if len(ans) == 0:
    print("TLE")
else:
    print(min(ans))
