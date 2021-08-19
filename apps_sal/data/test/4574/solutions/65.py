from collections import Counter as C
_ = input()
a = C([int(x) for x in input().split()])
b = []
for (k, v) in a.items():
    if 4 <= v:
        b.append(k)
    if 2 <= v:
        b.append(k)
else:
    if len(b) <= 1:
        print(0)
    else:
        b.sort()
        print(b[-1] * b[-2])
