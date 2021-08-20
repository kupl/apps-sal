import math
import collections
n = int(input())
factorial = 1
divisor = []
ans = 1


def get_prime(num):
    if num <= 1:
        return
    for i in range(2, num + 1):
        while num % i == 0:
            divisor.append(i)
            num //= i


for j in range(2, n + 1):
    get_prime(j)
count = collections.Counter(divisor)
for k in count.most_common():
    temp = list(k)[1]
    ans = ans * (temp + 1)
ans = ans % (10 ** 9 + 7)
print(ans)
