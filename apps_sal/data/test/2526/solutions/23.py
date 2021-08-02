x, y, a, b, c = map(int, input().split())
p = sorted(map(int, input().split()))
q = sorted(map(int, input().split()))
r = sorted(map(int, input().split()))
ans = p[-x:] + q[-y:] + r
ans.sort()
n = len(ans)
cnt = 0
for i in range(x + y):
    cnt += ans[n - 1 - i]
print(cnt)
