n = int(input())
sp = []
for i in range(n):
    (s, p) = input().split()
    p = int(p)
    sp.append((i + 1, s, p))
l = sorted(sp, key=lambda x: (x[1], -x[2]))
for (a, b, c) in l:
    print(a)
