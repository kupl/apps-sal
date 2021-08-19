class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        dic = collections.defaultdict(int)
        for i in range(len(A)):
            dic[A[i]] += 1
        ki = list(dic.keys())
        ki.sort(key=lambda x: abs(x))
        for k in ki:
            if dic[2 * k] < dic[k]:
                return False
            dic[2 * k] -= dic[k]
            dic[k] = 0
        return True
