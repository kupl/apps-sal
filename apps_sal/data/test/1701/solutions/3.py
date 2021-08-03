n, m = map(int, input().split())
d = {}
for i in range(n):
    s = input()
    s = s.split()
    d[s[1]] = s[0]
ans = []
for i in range(m):
    s = input()
    s = s.split()
    ip = s[1][:-1]
    ans.append('{} #{}'.format(' '.join(s), d[ip]))
for a in ans:
    print(a)
