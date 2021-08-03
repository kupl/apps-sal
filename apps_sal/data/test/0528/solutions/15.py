n, m = map(int, input().split())
v = [0] * 150005
s = [set([i])for i in range(150005)]
for _ in ' ' * m:
    a, b = map(int, input().split())
    s[a].add(b)
    s[b].add(a)
for i in range(n):
    if not v[i]:
        for j in s[i]:
            v[j] = 1
            if s[j] != s[i]:
                print('NO')
                return
print('YES')
