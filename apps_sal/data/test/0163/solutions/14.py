n, k = map(int, input().split())
s = input()
a = []
g = 0
t = 0
for i in range(n):
    if s[i] == '#':
        a.append(i)
    if s[i] == 'G':
        g = i
    if s[i] == 'T':
        t = i
if abs((t - g) % k != 0):
    print("NO")
    raise SystemExit
if t > g:
    for i in range(g, t, k):
        if i in a:
            print("NO")
            raise SystemExit
else:
    for i in range(t, g, k):
        if i in a:
            print("NO")
            raise SystemExit
print("YES")
