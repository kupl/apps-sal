n, m = map(int, input().split())
s = []
c = []
ans = [0] * n
if n > 1:
    ans[0] = 1
check = [10] * n
f = False
for _ in range(m):
    a, b = map(int, input().split())
    s.append(a)
    c.append(b)
for i in range(m):
    if n > 1 and s[i] == 1 and c[i] == 0:
        f = True
        break
    if check[s[i] - 1] != c[i] and check[s[i] - 1] != 10:
        f = True
        break
    ans[s[i] - 1] = c[i]
    check[s[i] - 1] = c[i]
if f:
    print("-1")
else:
    print("".join([str(a) for a in ans]))
