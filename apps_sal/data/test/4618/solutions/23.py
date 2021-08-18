s = input()
k = int(input())
n = len(s)

c = set()
for i in range(n):
    t = s[i:i + 5]
    for j in range(1, 5 + 1):
        c.add(t[:j])

c = list(c)
c.sort()
print((c[k - 1]))
