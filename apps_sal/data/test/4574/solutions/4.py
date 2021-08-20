from collections import Counter as C
_ = input()
a = C([int(x) for x in input().split()])
b = []
for (k, v) in a.items():
    b.extend([k] * (v // 2))
else:
    if 2 <= len(b):
        b.sort()
        print(b[-1] * b[-2])
    else:
        print(0)
