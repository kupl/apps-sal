class Solution:
    def minOperations(self, nums: List[int]) -> int:
        lst = list(map(find_op, nums))
        mul = max(lst, key=lambda x: x[0])
        mul = mul[0]
        add = sum([item[1] for item in lst])
        return add + mul


def find_op(n):
    mul, add = 0, 0
    while n > 0:
        if n % 2 == 1:
            add += 1
        n //= 2
        mul += 1
    if mul > 0:
        mul -= 1
    return mul, add
