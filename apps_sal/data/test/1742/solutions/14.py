from sys import stdin
n, m = list(map(int, stdin.readline().strip().split()))
s = list(map(int, stdin.readline().strip().split()))
nas = s[-1]
g = set()
st = set()
for i in range(m):
    a, b = list(map(int, stdin.readline().strip().split()))
    if b == nas:
        g.add(a)
    else:
        st.add((a, b))
x = n - 2
while x >= 0:
    if s[x] in g and s[x + 1] not in g and (s[x], s[x + 1]) in st:
        st.remove((s[x], s[x + 1]))
        aux = s[x]
        s[x] = s[x + 1]
        s[x + 1] = aux
        x = min(n - 2, x + 1)

    elif s[x] in g and s[x + 1] in g and (s[x], s[x + 1]) in st:
        st.remove((s[x], s[x + 1]))
        aux = s[x]
        s[x] = s[x + 1]
        s[x + 1] = aux
        x = min(n - 2, x + 1)

    else:
        x -= 1
ans = 0
for i in range(n - 2, -1, -1):
    if s[i] in g:
        ans += 1
    else:
        break
print(ans)
