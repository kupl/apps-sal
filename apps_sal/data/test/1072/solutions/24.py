(n, m) = map(int, input().split())
ans = 0
st = [input() for i in range(n)]
new = [''] * n
for i in range(m):
    newstr = [new[j] + st[j][i] for j in range(n)]
    if newstr == sorted(newstr):
        new = newstr
    else:
        ans += 1
print(ans)
