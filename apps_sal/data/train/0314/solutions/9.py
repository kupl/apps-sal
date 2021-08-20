class Solution:

    def numSub(self, s: str) -> int:
        num_lst = []
        ans = 0
        temp = 0
        for n in s:
            if n == '1':
                temp += 1
            if n == '0' and temp != 0:
                num_lst.append(temp)
                temp = 0
        if temp != 0:
            num_lst.append(temp)
        if len(num_lst) == 0:
            return 0
        for num in num_lst:
            while num != 0:
                ans += num
                num -= 1
        return ans % (10 ** 9 + 7)
