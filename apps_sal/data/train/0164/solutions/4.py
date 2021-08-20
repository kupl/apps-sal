class Solution:

    def minInteger(self, num: str, k: int) -> str:
        min_num = ''.join(sorted(list(num)))
        i = 0
        to_find = 0
        while num != min_num and k > 0 and (i < len(num)):
            index = num.find(str(to_find), i)
            while index != -1:
                if index - i <= k:
                    num = num[:i] + num[index] + num[i:index] + num[index + 1:]
                    k -= index - i
                    i += 1
                    to_find = 0
                    index = num.find(str(to_find), i)
                else:
                    break
            to_find += 1
        return num
