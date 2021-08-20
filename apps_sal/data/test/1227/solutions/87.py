from math import factorial
from itertools import product
S = input()
N = int(S)
m = len(S)
K = int(input())
product_K = product(['1', '2', '3', '4', '5', '6', '7', '8', '9'], repeat=K)
product_K = [int(''.join(x)) for x in product_K]
ans = len([x for x in product_K if x <= N])
if m > K:
    for i in range(1, m - K):
        ans += 9 ** K * factorial(i + K - 1) // factorial(i) // factorial(K - 1)
    zero_n = m - K
    non_zero_n = K
    for i in range(m):
        l = int(S[i])
        if l == 0:
            zero_n -= 1
            continue
        if i > 0 and zero_n > 0:
            ans += 9 ** non_zero_n * factorial(zero_n - 1 + non_zero_n) // factorial(zero_n - 1) // factorial(non_zero_n)
        non_zero_n -= 1
        ans += len([x for x in range(1, l)]) * 9 ** non_zero_n * factorial(zero_n + non_zero_n) // factorial(zero_n) // factorial(non_zero_n)
        if non_zero_n <= 0:
            ans += 1
            break
print(ans)
