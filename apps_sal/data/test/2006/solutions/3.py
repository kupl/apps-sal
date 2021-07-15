n, m = map(int, input().split())
c = 0
g = 0
t = set()
f = False
for i in range(n):
    s = input().strip()
    for j in range(len(s)):
        if s[j] == 'G':
            g = j
        elif s[j] == 'S':
            c = j
    if g - c > 0:
        print(-1)
        f = True
        break
    t.add(c - g)
if not f:
    print(len(t))
