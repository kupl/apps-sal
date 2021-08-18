n, m = map(int, input().split())
d = {}
for i in range(n):
    t = input()
    t = t.split()
    s = t[1]
    d[s] = t[0]
for i in range(m):
    t = input()
    s = t.split()[1][:-1]
    t += '
    print(t)
