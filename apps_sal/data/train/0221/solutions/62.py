class Solution:

    def searchLongestStringOfKLen(self, S, total_len, compare_len):
        search_len_hash = 0
        for i in range(compare_len):
            search_len_hash = (search_len_hash * self.uniq + self.nums[i]) % self.mod
        tmp_hash = {}
        tmp_hash[search_len_hash] = True
        remove_old_power = pow(self.uniq, compare_len, self.mod)
        for i in range(1, total_len - compare_len + 1):
            search_len_hash = (search_len_hash * self.uniq - remove_old_power * self.nums[i - 1] + self.nums[i + compare_len - 1]) % self.mod
            if search_len_hash in tmp_hash:
                return i
            tmp_hash[search_len_hash] = True
        return -1

    def longestDupSubstring(self, S: str) -> str:
        ls = len(S)
        end = ls
        start = 1
        mid = 0
        self.nums = []
        for i in range(ls):
            self.nums.append(ord(S[i]) - ord('a'))
        self.uniq = 26
        self.mod = 2 ** 32
        while start <= end:
            mid = start + (end - start) // 2
            if self.searchLongestStringOfKLen(S, ls, mid) != -1:
                start = mid + 1
            else:
                end = mid - 1
        ds_sp = self.searchLongestStringOfKLen(S, ls, start - 1)
        return S[ds_sp:ds_sp + start - 1]
