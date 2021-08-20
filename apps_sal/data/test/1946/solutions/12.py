n = int(input())
sum1 = 0
fo = dict()
for i in range(n):
    (x, y) = map(int, input().split())
    fo[x] = y
    sum1 += y
to = dict()
m = int(input())
for i in range(m):
    (x, y) = map(int, input().split())
    if x in fo:
        if fo[x] < y:
            sum1 -= fo[x]
            sum1 += y
    else:
        sum1 += y
print(sum1)
