n = int(input())
nums = list(map(int, input().split()))


def factorize(n):
    if n == 1:
        raise('n >= 2')
    
    factor = {}
    div = 2
    while True:
        if div * div > n:
            factor[n] = factor.get(n, 0) + 1
            return factor

        if n % div == 0:
            n //= div
            factor[div] = factor.get(div, 0) + 1
        else:
            div += 1


def factor_product(a, b):
    '''
    素因数分解のdict a, bを受け取って、
    積に対応するdictを返す
    '''
    product = a.copy()
    for k, v in list(b.items()):
        product[k] = product.get(k, 0) + v
    return product

import math

summ = 1
b = 1
mod = 10**9 + 7

for idx in range(1, n):
    temp = b * nums[idx-1]
    gcd = math.gcd(temp, nums[idx])
    multiple = nums[idx] // gcd
    summ *= multiple

    b = b * nums[idx-1] * multiple // nums[idx]
    summ += b
    summ %= mod

print(summ)

