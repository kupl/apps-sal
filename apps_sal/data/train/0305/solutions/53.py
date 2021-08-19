class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        res = set()                                           # keep distinct
        for i in range(len(text)):                            # i: start index
            for l in range(1, len(text) - i):                    # l: length of the repeated string
                if text[i] == text[i + l]:                      # only check if the first character matches
                    k = 1                                     # k: repeated times
                    while i + (k + 1) * l <= len(text):
                        if text[i:i + k * l] == text[i + k * l:i + (k + 1) * l]:
                            res.add(text[i:i + (k + 1) * l])
                            k *= 2                            # double the count and continue checking
                        else:
                            break
        return len(res)
