class Solution:

    def largestMultipleOfThree(self, d: List[int]) -> str:
        d1 = sorted([i for i in d if i % 3 == 1])
        d2 = sorted([i for i in d if i % 3 == 2])
        d3 = [i for i in d if i % 3 == 0]
        if sum(d) % 3 == 1:
            if len(d1) != 0:
                res = d1[1:] + d2 + d3
            else:
                res = d2[2:] + d3
        elif sum(d) % 3 == 2:
            if len(d2) != 0:
                res = d1 + d2[1:] + d3
            else:
                res = d1[2:] + d3
        else:
            res = d
        res.sort(reverse=True)
        if not res:
            return ''
        return str(int(''.join([str(i) for i in res])))
