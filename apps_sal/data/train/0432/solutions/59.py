import collections


class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        if len(nums) == 0:
            return False
        if len(nums) % k != 0:
            return False
        numSets = len(nums) // k
        freqCnt = dict()
        for i in nums:
            if i not in freqCnt:
                freqCnt[i] = 1
            else:
                freqCnt[i] += 1
        keys = sorted(freqCnt.keys())
        for i in range(numSets):
            smallest = keys[0]
            cursor = None
            remain = k - 1
            freqCnt[smallest] -= 1
            if freqCnt[smallest] == 0:
                keys.pop(0)
                cursor = 0
            else:
                cursor = 1
            while cursor < len(keys) and remain != 0:
                if keys[cursor] == smallest + 1:
                    smallest = keys[cursor]
                    remain -= 1
                    freqCnt[smallest] -= 1
                    if freqCnt[smallest] == 0:
                        keys.pop(cursor)
                    else:
                        cursor += 1
                else:
                    return False
            if cursor == len(keys) and remain != 0:
                return False
        return True
