class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        dic = dict()
        for x in nums:
            if x not in dic:
                dic[x] = 0
            dic[x] += 1
        hulu = sorted(list(dic.keys()))
        dahulu = [0]
        for x in hulu:
            dahulu.append(dahulu[-1] + dic[x])
        dahulu = dahulu[1:]

        output = 0

        start = 0
        end = len(hulu) - 1
        while start < len(hulu):
            while end >= start:
                if hulu[start] + hulu[end] <= target:
                    output += (2**dic[hulu[start]] - 1) * (2**(dahulu[end] - dahulu[start]))
                    break
                else:
                    end -= 1
            start += 1

        return output % (10**9 + 7)
