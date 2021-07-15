class Solution:
    def maxRepOpt1(self, text: str) -> int:
        c = Counter(text)
        window = Counter()
        i = 0
        ans = 1
        for j in range(len(text)):
            c[text[j]] -= 1
            window[text[j]] += 1
            while not (len(window) == 1 or (len(window) == 2 and min(window.values()) == 1)):
                c[text[i]] += 1
                window[text[i]] -= 1
                if window[text[i]] == 0:
                    del window[text[i]]
                i += 1
            if len(window) == 1 or c[sorted(window, key=window.get)[1]] > 0:
                ans = max(ans, j - i + 1)
        return ans       
