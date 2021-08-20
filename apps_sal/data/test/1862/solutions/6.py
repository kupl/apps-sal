n = int(input())
x = list(map(int, input().split()))
a = [0] * n
cur = 0
res = 0
for y in x:
    m = y - 1
    if a[m]:
        a[m] = 0
        cur -= 1
    else:
        a[m] = 1
        cur += 1
        res = max(res, cur)
print(res)
