# ATTENTION:
# never attend codeforces if u're drunk
n = int(input())
a = sorted([int(x) for x in input().split()])
c = dict()
for x in a:
    c[x] = c[x] + 1 if x in c else 1
uniq = sorted(c.keys())
C = 0
while n > 0:
    t = 0
    for u in uniq:
        if c[u] == 0:
            continue
        c[u] -= 1
        n -= 1
        t += 1
    C += t - 1
print(C)
