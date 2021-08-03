def read(): return list(map(int, input().split()))


n, s = read()
ans = s
for i in range(n):
    f, t = read()
    ans = max(ans, f + t)
print(ans)
