from collections import defaultdict

n = int(input())

is_first = []
d = defaultdict(int)
ans = 0

for _ in range(n):
    s = input()
    slen = len(s)
    for i in range(slen):
        t = s[i]
        if i == 0:
            if t not in is_first:
                is_first.append(t)
        num = 10 ** (slen - i - 1)
        d[t] += num


l = sorted(list(d.items()), key=lambda v: v[1], reverse=True)

for i,x in enumerate(l):
    if x[0] not in is_first:
        l.pop(i)
        break

for i,x in enumerate(l):
    ans += x[1] * (i+1)

print(ans)



