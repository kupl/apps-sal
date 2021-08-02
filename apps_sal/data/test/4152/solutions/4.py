n = int(input())
a = [int(x) for x in input().split()]
a2 = [2 << k for k in range(32)]
d = dict()
for c in a:
    d[c] = d.setdefault(c, 0) + 1
cnt = 0
for c in a:
    cnt += 1
    for c2 in a2:
        if c2 > c and c2 - c in d.keys():
            if c2 - c != c or d[c] != 1:
                cnt -= 1
                break
print(cnt)
