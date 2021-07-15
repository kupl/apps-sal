class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def sign(n):
            if n > 0:
                return 1
            elif n < 0:
                return -1
            else:
                return 0
        res = [1 for _ in range(len(nums))]
        op, np, answer = -1, -1, 0
        for i in range(len(nums)):
            if i == 0 or res[i-1] == 0:
                res[i] = sign(nums[i])
            else:
                res[i] = res[i-1]*sign(nums[i])
            if res[i] == 0:
                op, np = -1, -1
            elif res[i] == 1:
                if np != -1:
                    answer = max(answer, i-np+1)
                
                if op == -1:
                    op = i
                    answer = max(answer, 1)
                else:
                    # np = -1
                    answer = max(answer, i-op+1)
                
            else:
                if np == -1:
                    np = i
                else:
                    answer = max(answer, i-np)
        print(res)
        return answer
