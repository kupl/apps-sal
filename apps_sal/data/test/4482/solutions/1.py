n = int(input())
a = [int(x) for x in input().split()]
res = 10 ** 9
for i in range(-100, 101):
    cc = 0
    for j in range(n):
        cc += (i - a[j]) ** 2
    res = min(res, cc)
print(res)
