class Solution:
    def countTriplets(self, A: List[int]) -> int:
        count =collections.defaultdict(int)
        ret = 0
        for i in A:
            for j in A:
                count[i & j] += 1
        for i in A:
            for j in count:
                if i & j == 0: ret += count[j]
        return ret
