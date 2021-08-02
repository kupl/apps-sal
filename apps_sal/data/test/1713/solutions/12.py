rd = lambda: list(map(int, input().split()))
n, s, t = rd()
A = rd()
cur = s
ans = 0
for i in range(n):
    if(cur == t):
        print(ans);
        return
    cur = A[cur - 1]
    ans = ans + 1
print(-1)
