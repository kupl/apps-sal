def div(n):
    c = 0
    i = 1
    k = 0
    if sqrt(n).is_integer():
        return 0
    while i * i < n and c <= 3:
        if n % i == 0:
            c += 1
            k += i + n // i
        i += 1
    if c == 2:
        return k
    else:
        return 0


class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans += div(i)
        return ans
