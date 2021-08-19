import math
import collections

n = int(input())

factorial = 1
divisor = []
ans = 1


# 素数を求める関数
def get_prime(num):
    if num <= 1:
        return
    for i in range(2, num + 1):
        while num % i == 0:
            divisor.append(i)
            num //= i


# 約数の数 = (素数xの個数+1)(素数yの個数+1)(素数zの個数+1)...
# 方針：入力値を素因数分解し、各素因数の個数を求める

# n-iの素因数を求める
for j in range(2, n + 1):
    get_prime(j)

# print(divisor)

# 各素因数の組み合わせ数を求める
count = collections.Counter(divisor)

for k in count.most_common():
    temp = list(k)[1]
    ans = ans * (temp + 1)

ans = ans % (10 ** 9 + 7)

print(ans)
