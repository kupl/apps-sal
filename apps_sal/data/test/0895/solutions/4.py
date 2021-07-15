n = int(input())
v = list(map(int, input().split()))
t = int(input())

v.sort()
ret = 1
lef = 0
rit = 1
while rit < n:
    while rit < n and v[rit] - v[lef] <= t:
        rit = rit + 1

    ret = max(ret, rit - lef)
    lef = lef + 1

print(ret)

