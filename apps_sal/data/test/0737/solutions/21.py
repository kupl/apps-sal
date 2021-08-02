from math import sqrt


def cal_add(x):
    return 2 if x > 0 else 0


n = int(input())
k = int(sqrt(n))
r = n - k ** 2
rs = k * 4
a = r if r <= k else r - k
b = r - a
rs += (cal_add(a) + cal_add(b))
print(rs)
