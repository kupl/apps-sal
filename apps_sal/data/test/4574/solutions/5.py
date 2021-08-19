from collections import Counter as C
_ = input()
a = C([int(x) for x in input().split()])
b = []
for (k, v) in a.items():
    for _ in range(v // 2):
        b.append(k)
else:
    if 2 <= len(b):
        b.sort()
        print(b[-1] * b[-2])
    else:
        print(0)
