
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False

        counter = collections.Counter(nums)
        keys = sorted(counter)
        print(keys)
        for i in keys:
            while i in counter:
                cur = i
                counter[cur] -= 1
                if not counter[cur]:
                    del counter[cur]
                for _ in range(k - 1):
                    if cur + 1 in counter:
                        cur += 1
                        counter[cur] -= 1
                        if not counter[cur]:
                            del counter[cur]
                    else:
                        return False
        return True
