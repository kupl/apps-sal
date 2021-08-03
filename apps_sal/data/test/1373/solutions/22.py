n, k = [int(x) for x in input().split()]
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = a[i - 1] + i
# print(a)
res = 0
for i in range(k, n + 1):
    ma = a[n] - a[n - i]
    mi = a[i - 1]
    res += ma - mi + 1
    # print(i,res,ma,mi)
res += 1
res %= 10 ** 9 + 7
print(res)
