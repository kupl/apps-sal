c1 = int(input())
c2 = int(input())
c3 = int(input())
c4 = int(input())

res = 1
if c1 != c4:
    res = 0
elif c3 > 0 and c1 == 0:
    res = 0

print(res)
