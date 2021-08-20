from collections import Counter
c1 = Counter()
c2 = Counter()
for _ in range(int(input())):
    s = input()
    p = 0
    q = 0
    for c in s:
        if c == '(':
            p += 1
        else:
            p -= 1
            q = min(q, p)
    if p == q:
        c1[-p] += 1
    elif q == 0:
        c2[p] += 1
print(sum((min(c1[k], c2[k]) for k in list(c1.keys()))) + c1[0] // 2)
