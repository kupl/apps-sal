class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(div):
            # print(sum([elem/div if elem % div == 0 else (elem//div)+1 for elem in nums]))
            return threshold >= sum([elem / div if elem % div == 0 else (elem // div) + 1 for elem in nums])

        def bst(low, high):
            # print(low,high)
            mid = (low + high) // 2
            if low > high:
                return -1
            elif low == high:
                if check(low):
                    return low
                else:
                    return -1
            else:
                if check(mid):
                    ambition = bst(low, mid - 1)
                    if ambition != -1:
                        return ambition
                    else:
                        return mid
                else:
                    return bst(mid + 1, high)

        return bst(1, 10**9)
