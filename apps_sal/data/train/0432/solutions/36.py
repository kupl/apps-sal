class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # if len(nums)%k!=0:
        #     return False
        # c=Counter(nums)
        # keys=sorted(c)
        # for key in keys:
        #     while c[key]>0:
        #         for i in range(k):
        #             if key+i in c.keys() and c[key+i]>0:
        #                 c[key+i]-=1
        #             else:
        #                 return False
        # return True

        c = Counter(nums)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(k)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True
