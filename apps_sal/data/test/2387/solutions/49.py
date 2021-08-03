from functools import reduce
n, *s = open(0).read().split()
u = []
for t in s:
    close_cnt = 0
    tmp = 0
    for c in t:
        tmp += (1 if c == '(' else -1)
        close_cnt = min(close_cnt, tmp)
    u.append((close_cnt, tmp - close_cnt))
M = 10**6 + 1
acc = 0
for a, b in sorted(u, key=lambda z: (- M - z[0] if sum(z) >= 0 else M - z[1])):
    if acc + a < 0:
        print("No")
        return
    else:
        acc += a + b
print(("No" if acc else "Yes"))
