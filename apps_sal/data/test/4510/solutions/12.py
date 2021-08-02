a = list(map(int, input().split()))
sc = a[1]
m = a[0]
a = list(map(int, input().split()))
d = {}
s = []
for i in a:
    if i in d: continue
    if len(s) < sc:
        s.append(i)
        d[i] = 1
    else:
        d.pop(s.pop(0))
        s.append(i)
        d[i] = 1
print(len(s))
print(*s[::-1])
