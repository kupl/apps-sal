class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        memo_dict = {}
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if j - i < minSize:
                    continue
                if j - i > minSize:
                    break
                temp = []
                temp_str = s[i:j]
                for char in temp_str:
                    temp.append(char)
                if len(set(temp)) > maxLetters:
                    continue

                if temp_str in memo_dict:
                    memo_dict[temp_str] += 1
                else:
                    memo_dict[temp_str] = 1

        if len(memo_dict) == 0:
            return 0
        res = sorted(memo_dict, key=lambda x: memo_dict[x])
        # print(res)
        return memo_dict[res[-1]]
