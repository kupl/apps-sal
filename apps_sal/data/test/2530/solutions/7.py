(w, x) = map(int, input().split())
s = {}
s1 = {}
s2 = {}
for i in range(w):
    (a, b) = input().split()
    s[a] = b
for i in range(x):
    a = input()
    s1[a] = s1.get(a, 0) + 1
    s2[s[a]] = s2.get(s[a], 0) + 1
m1 = max(s2.values())
c = []
for (a, b) in s2.items():
    if b == m1:
        c.append(a)
print(min(c))
r = max(s1.values())
d = []
for (a, b) in s1.items():
    if b == r:
        d.append(a)
print(min(d))
