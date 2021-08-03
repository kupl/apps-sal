class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        counter = collections.Counter(A)
        counter = dict(sorted(counter.items(), key=lambda x: abs(x[0])))
        nums = []
        for num in counter.keys():
            for _ in range(counter[num]):
                nums.append(num)
        for num in nums:
            if counter[num]:
                if 2 * num in counter and counter[2 * num] != 0:
                    counter[num] -= 1
                    counter[num * 2] -= 1
                else:
                    return False
        return True
