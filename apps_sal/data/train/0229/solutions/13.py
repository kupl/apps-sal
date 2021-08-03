class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        result = True
        numLen = len(A)
        C = Counter(A)
        val = list(C.keys())
        val.sort()
        for i in range(len(val)):
            if val[i] < 0:
                if val[i] % 2 == 0:
                    if val[i] / 2 in val and C[val[i] / 2] >= C[val[i]]:
                        C[val[i] / 2] = C[val[i] / 2] - C[val[i]]
                        C[val[i]] = 0
                    else:
                        result = False
                        # break
            else:
                if val[i] * 2 in val and C[val[i] * 2] >= C[val[i]]:
                    C[val[i] * 2] = C[val[i] * 2] - C[val[i]]
                    C[val[i]] = 0
                else:
                    result = False
                    # Break
        nums = list(C.values())
        if nums == [0] * len(nums):
            result = True
        else:
            result = False
        return result
