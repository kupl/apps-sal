class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict
        letters = defaultdict(int)
        res = 0
        if len(s) < minSize:
            return 0
        i = 0
        j = 0
        unique = 0
        counter = defaultdict(int)
        while i < len(s):
            if letters[s[i]] == 0:
                unique += 1
            letters[s[i]] += 1
            
            while j < i and unique > maxLetters:
                letters[s[j]] -= 1
                if letters[s[j]] == 0:
                    unique -= 1
                j += 1
            j_tmp = j
            unique_tmp = unique
            letters_tmp = letters.copy()
            while unique_tmp <= maxLetters and (minSize <= (i - j_tmp + 1)):
                if (i - j_tmp + 1) > maxSize:
                    j_tmp+=1
                    continue
                counter[s[j_tmp:i+1]] += 1
                #print(f'{s[j_tmp:i+1]} {counter} {i} {j_tmp}')
                letters_tmp[s[j_tmp]] -= 1
                if letters_tmp[s[j_tmp]] == 0:
                    unique_tmp -= 1
                j_tmp += 1
                #print(f'i {i} j {j} unique {unique} {s[j:i+1]} letters {letters},res {res}, len {i-j+1}, {counter}')
            i += 1
        if len(counter.values()) == 0:
            return 0
        
        return max(counter.values())
