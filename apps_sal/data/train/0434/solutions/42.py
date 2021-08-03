class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        se = set(nums)
        if(0 not in se):
            return len(nums) - 1
        elif(1 not in se):
            return 0

        count = 0
        flag = 0
        ls = []
        for i in nums:
            if(i == 0):
                if(flag == 0):
                    count += 1
                else:
                    flag = 0
                    ls.append(count)
                    count = 1
            else:
                if(flag == 1):
                    count += 1
                else:
                    flag = 1
                    ls.append(count)
                    count = 1
        ls.append(count)
        # print(ls)
        ind = 0
        ans = 0
        while(ind < len(ls)):
            if(ls[ind] != 0):
                if(ls[ind] == 1):
                    if(ind == 0 and ind < len(ls) - 1):
                        ans = max(ans, ls[ind + 1])
                    elif(ind == len(ls) - 1 and ind > 0):
                        ans = max(ans, ls[ind - 1])
                    else:
                        if(ind < len(ls) - 1 and ind > 0):
                            ans = max(ans, ls[ind - 1] + ls[ind + 1])
                else:
                    if(ind == 0 and ind < len(ls) - 1):
                        ans = max(ans, ls[ind + 1])
                    elif(ind == len(ls) - 1 and ind > 0):
                        ans = max(ans, ls[ind - 1])
                    else:
                        if(ind < len(ls) - 1 and ind > 0):
                            ans = max(ans, max(ls[ind - 1], ls[ind + 1]))
            # print(ans,ind)
            ind += 2

        return ans
