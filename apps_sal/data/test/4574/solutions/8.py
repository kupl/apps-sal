from collections import Counter as C

_ = input()
a = C([int(x) for x in input().split()])

b = [0, 0]
for k, v in a.items():
    b.extend([k] * (v // 2))
else:
    b.sort()
    print(b[-1] * b[-2])
