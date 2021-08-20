class Solution:

    def maxRepOpt1(self, text: str) -> int:
        letters = {}
        for (i, char) in enumerate(text):
            if char in letters:
                letters[char].append(i)
            else:
                letters[char] = [i]
        if len(letters) == 1:
            return len(text)
        ans = 0
        for letter in letters:
            cur = 0
            prev = 0
            discarded = False
            maxSoFar = 0
            arr = letters[letter]
            for (j, pos) in enumerate(arr):
                if not j:
                    cur = 1
                elif pos - arr[j - 1] == 1:
                    cur += 1
                else:
                    if not discarded and prev:
                        discarded = True
                    elif not discarded and pos - arr[j - 1] > 2:
                        discarded = True
                    if prev + cur > maxSoFar:
                        maxSoFar = prev + cur
                    if pos - arr[j - 1] == 2:
                        prev = cur
                        cur = 1
                    else:
                        prev = 0
                        cur = 1
            print(prev + cur)
            if prev + cur > maxSoFar:
                maxSoFar = prev + cur
            if discarded:
                maxSoFar += 1
            if maxSoFar > ans:
                ans = maxSoFar
        return ans
