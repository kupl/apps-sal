n = int(input())
a = {}
for i in range(n):
    s = str(input())
    if s in a.keys():
        a[s] = a[s] + 1
    else:
        a[s] = 1
m = int(input())
for i in range(m):
    t = str(input())
    if t in a.keys():
        a[t] = a[t] - 1
    else:
        a[t] = -1
if max(a.values()) >= 0:
    print(max(a.values()))
elif max(a.values()) < 0:
    print(0)
