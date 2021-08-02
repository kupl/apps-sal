R = lambda: list(map(int, input().strip().split()))
[x, y, l, r] = R()
a = list()
b = list()
cur = 1
while(cur < r):
    a.append(cur)
    cur *= x
cur = 1
while(cur < r):
    b.append(cur)
    cur *= y

s = set()
s.add(l - 1)
s.add(r + 1)
for p in a:
    for q in b:
        s.add(p + q)
s = list(s)
s.sort()
ml = 0
for i in range(len(s) - 1):
    if s[i] >= l - 1 and s[i + 1] <= r + 1:
        ml = max(ml, s[i + 1] - s[i] - 1)
print(ml)
