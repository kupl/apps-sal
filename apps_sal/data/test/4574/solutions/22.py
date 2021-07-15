from collections import Counter as C

_ = input()
a = C([int(x) for x in input().split()])

b = [0] * 2
for k, v in a.items():
    if 4 <= v:
        b.append(k)
    if 2 <= v:
        b.append(k)
else:
    b.sort()
    print(b[-1] * b[-2])
