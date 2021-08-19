(a, b) = [int(x) for x in input().split()]
res = 0
c = 1
while c < b:
    c += a - 1
    res += 1
print(res)
