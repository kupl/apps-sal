class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        maks = 0
        string = ''
        count = 0
        lenght = 0
        for l in s:
            if l == 'a' or l == 'e' or l == 'i' or (l == 'o') or (l == 'u'):
                count += 1
            string += l
            lenght += 1
            if lenght == k:
                if count > maks:
                    maks = count
                if string[0] == 'a' or string[0] == 'e' or string[0] == 'i' or (string[0] == 'o') or (string[0] == 'u'):
                    count -= 1
                lenght -= 1
                string = string[1:k]
        return maks
