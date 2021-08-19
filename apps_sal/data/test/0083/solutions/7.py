n = int(input())
l = sorted([*list(map(int, input().split()))])
p = sum((1 for e in l if e > 0))
neg = sum((1 for e in l if e < 0))
if p >= (n + 1) // 2:
    res = 1
elif neg >= (n + 1) // 2:
    res = -1
else:
    res = 0
print(res)
