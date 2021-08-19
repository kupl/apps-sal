from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


(n, k) = map(int, input().split())
lst = []
kk = k
i = 2
while i <= kk:
    c = 0
    while kk % i == 0:
        c += 1
        kk //= i
    if c:
        lst.append([i, c])
    i += 1
arr = list(map(int, input().split()))
flag = True
for j in lst:
    ma = 0
    for i in range(n):
        c = 0
        while arr[i] % j[0] == 0:
            c += 1
            arr[i] //= j[0]
        ma = max(c, ma)
    if ma < j[1]:
        flag = False
        break
print('Yes') if flag else print('No')
