n = int(input())
a = [int(x) for x in input().split()]
result = 0
for (i, x) in enumerate(a):
    flg = True
    for c in a[:i]:
        flg = flg and c <= x
    if flg:
        result += 1
print(result)
