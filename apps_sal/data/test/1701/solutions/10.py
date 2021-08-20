(n, m) = map(int, input().split())
s = dict()
for x in range(n):
    (name, ip) = input().split()
    s[ip] = name
for y in range(m):
    (a, b) = input().split()
    c = b[:-1]
    print(a, b, '#' + s[c])
