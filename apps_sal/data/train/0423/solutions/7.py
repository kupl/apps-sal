class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        current = {}
        for x in arr:
            old = x - difference
            if old in current:
                count = current[old]
                del current[old]
                current[x] = count + 1
            elif x not in current:
                current[x] = 1
            #print(f'{x, current}')
        return max(current.values())

