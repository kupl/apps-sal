class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        word_dic = {}
        str_dic = {}
        r_end = 0
        ans = 0

        def update_ans(length):
            if length >= minSize:
                return min(length, maxSize) - minSize + 1
            return 0

        for i in range(len(s)):
            while (r_end < len(s)):
                ch = s[r_end]
                if ch in list(word_dic.keys()):
                    word_dic[ch] += 1
                else:
                    if len(list(word_dic.keys())) < maxLetters:
                        word_dic[ch] = 1
                    else:
                        break
                r_end += 1
            for j in range(minSize, min(maxSize, r_end - i) + 1):
                subs = s[i:i + j]
                if subs not in str_dic:
                    str_dic[subs] = 1
                else:
                    str_dic[subs] += 1
            word_dic[s[i]] -= 1
            if word_dic[s[i]] == 0:
                del word_dic[s[i]]
        if not bool(str_dic):
            return 0
        else:
            return max(str_dic.values())
