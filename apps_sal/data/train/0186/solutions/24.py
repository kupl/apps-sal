def dp(costs, target, mem):
    if target == 0:
        return ''
    elif target in mem:
        return mem[target]
    res = ''
    for i in range(len(costs)):
        if target - costs[i] >= 0:
            current = dp(costs, target - costs[i], mem)
            if current is not None:
                res = max([res, str(i + 1) + current], key=lambda x: (len(x), x))
    mem[target] = res if res != '' else None
    return res if res != '' else None


class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        result = dp(cost, target, {})
        return result if result != '' and result is not None else '0'
