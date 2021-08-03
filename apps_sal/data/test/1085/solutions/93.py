import numpy as np
n = int(input())

# n % k = 1 の数
m = n - 1
i = 2
ans = 1
while i * i <= m:
    if m % i == 0:
        num = 1
        while m % i == 0:
            num += 1
            m //= i
        ans *= num
    i = i + 1
if m != 1:
    ans *= 2
ans -= 1

# n % k = 0 の場合
# nを素因数分解する
m = n
i = 2
factor = []
while i * i <= n:
    if n % i == 0:
        l = []
        num = 1
        l.append(num)
        while n % i == 0:
            num *= i
            l.append(num)
            n //= i
        factor.append(np.array(l))
    i = i + 1
if n > 1:
    factor.append(np.array([1, n]))

# 直積を求めることでnの全約数を得る
divisor = factor[-1]
for i in range(len(factor) - 1):
    divisor = np.outer(divisor, factor[i])
divisor = np.outer(np.array(1), divisor)

# 判定
for i in divisor[0]:
    if i == 1:
        continue
    n = m
    while n % i == 0:
        n //= i
    if n % i == 1:
        ans += 1

print(ans)
