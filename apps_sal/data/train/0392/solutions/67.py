class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        mod = 10 ** 9 + 7
        nums1 = sum(1 if s[i] == '1' else 0 for i in range(n))
        if nums1 % 3 != 0:
            return 0
        num_per = nums1 // 3
        if num_per == 0:
            res = 0
            for i in range(1, n - 1):
                res = (res + (n - 1 - i)) % mod
            return res

        def find_end(start, num1):
            count = 0
            index = start
            while index < n and count < num1:
                if s[index] == '1':
                    count += 1
                index += 1
            return index - 1
        end1 = find_end(0, num_per)
        i = end1 + 1
        while s[i] != '1':
            i += 1
        end2 = find_end(i, num_per)
        j = end2 + 1
        while s[j] != '1':
            j += 1
        return ((i - end1) * (j - end2)) % mod
