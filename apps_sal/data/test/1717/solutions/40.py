import math
N = int(input())
prime_factor = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def find_prime_factor(n, ans):
    for i in prime_factor:
        ni = 0
        nn = n
        while nn % i == 0:
            ni += 1
            nn /= i
        if ans[i] < ni:
            ans[i] = ni
    return ans


ans = dict(list(zip(prime_factor, [0] * len(prime_factor))))
for i in range(2, N + 1):
    ans = find_prime_factor(i, ans)
ret = 1
for i in ans:
    ret = ret * i ** ans[i]
ret += 1
print(ret)
