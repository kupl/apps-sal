def read(): return list(map(int, input().split()))


n, m = read()
c = [tuple(read()) for i in range(n)]
ans = 0
for i in range(n):
    cur = min(c[i])
    if cur > ans:
        ans = cur
print(ans)
