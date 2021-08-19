from collections import Counter
_ = input()
a = list(map(int, input().split()))
c = Counter(a)
s = sum(a)
r = []
for (i, e) in enumerate(a, 1):
    if (s - e) % 2 == 0 and (s - e) / 2 in c and ((s - e) / 2 != e or c[e] > 1):
        r.append(i)
print(len(r))
if len(r) != 0:
    print(*r)
