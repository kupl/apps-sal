from sys import stdin, stdout, exit

t1, t2, t3 = stdin.readline().split()

if t1 == t2 and t2 == t3:
    print(0)
    return

ts = [(int(t[0]), t[1]) for t in [t1, t2, t3]]
ts.sort()
ns = [t[0] for t in ts]
ss = [t[1] for t in ts]

if ns[0] + 1 == ns[1] and ns[0] + 2 == ns[2] and ss[0] == ss[1] and ss[1] == ss[2]:
    print(0)
    return
if ns[0] + 2 >= ns[1] and ss[1] == ss[0]:
    print(1)
    return
if ns[1] + 2 >= ns[2] and ss[1] == ss[2]:
    print(1)
    return
if ns[0] + 2 >= ns[2] and ss[0] == ss[2]:
    print(1)
    return
if ts[0] == ts[1] or ts[1] == ts[2] or ts[2] == ts[0]:
    print(1)
    return

print(2)
