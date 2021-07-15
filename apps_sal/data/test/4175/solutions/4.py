n = int(input())
s = set()

ok = True
t = input()
p = t[-1]
s.add(t)
for i in range(n-1):
    t = input()
    if t in s:
        ok = False
    s.add(t)
    if t[0] != p:
        ok = False
    p = t[-1]

print(('Yes' if ok else 'No'))

