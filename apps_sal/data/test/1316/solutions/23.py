(n, k) = (int(i) for i in input().split())
s = input()
D = {}
for i in s:
    D[i] = []
a = s[0]
c = 1
for i in range(1, len(s)):
    if s[i] == a:
        c += 1
    else:
        D[a].append(c)
        a = s[i]
        c = 1
D[a].append(c)
m = 0
x = 0
for i in list(D.keys()):
    for j in D[i]:
        x += j // k
    if x > m:
        m = x
    x = 0
print(m)
