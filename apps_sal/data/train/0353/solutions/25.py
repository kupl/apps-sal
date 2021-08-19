p = 1000000007


def modSum(a, b):
    return (a + b) % p


def modProd(a, b):
    return a * b % p


def modPow(x, n):
    if n == 0:
        return 1
    res = modPow(x, n // 2)
    res = modProd(res, res)
    if n % 2 == 1:
        res = modProd(res, x)
    return res


class Solution:

    def numSubseq(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        i = 0
        j = n - 1
        res = 0
        while i <= j:
            sum = arr[i] + arr[j]
            if sum > target:
                j -= 1
            else:
                res = modSum(res, modPow(2, j - i))
                i += 1
        return res
