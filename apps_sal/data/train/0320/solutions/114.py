def get_num_ops(num):
    assert num >= 0
    d_ops, s_ops = 0, 0
    while num != 0:
        if num % 2 == 1:
            num = num - 1
            s_ops += 1
        else:
            num = num // 2
            d_ops += 1
    return d_ops, s_ops


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_ops = 0
        doubling_ops = []
        for num in nums:
            d, s = get_num_ops(num)
            doubling_ops.append(d)
            num_ops += d + s
            print(num_ops)

        doubling_ops = sorted(doubling_ops)
        change = [doubling_ops[0]]
        for i in range(1, len(doubling_ops)):
            change.append(doubling_ops[i] - doubling_ops[i - 1])

        for i, c in enumerate(change):
            num_ops = num_ops - c * (len(change) - i - 1)

        return num_ops
