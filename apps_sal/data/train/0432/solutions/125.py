class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)

        if len(count):
            start = min(count)

            while len(count):
                # print(count)
                if count[start] == 0:
                    start = min(count)
                for num in range(start, start + k):
                    if count[num]:
                        count[num] -= 1
                    else:
                        return False
                    if count[num] == 0:
                        del count[num]
                        start += 1

            return True

        return False
