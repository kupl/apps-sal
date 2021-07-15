n = int(input())

a = [int(x) for x in input().split()]
a.sort()

cur = 0
res = 0
for x in a:
    if x >= cur:
        res += 1
        cur += x

print(res)
