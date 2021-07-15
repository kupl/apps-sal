from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        if len(text) == 1:
            return 1
        counts = Counter(text)
        # a b a b a.
        pre = [1]
        nex = [1]
        ans = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                pre.append(pre[-1] + 1)
            else :
                pre.append(1)
            ans = max(pre[i], ans)
                
        for i in range(len(text) - 2, -1, -1):
            if text[i] == text[i + 1]:
                nex.append(nex[-1] + 1)
            else:
                nex.append(1)
            ans = max(nex[len(text) - i - 1], ans)
        nex.reverse()
        
        # Now try some swaps.
        for i in range(len(text)):
            # We will try to swap out i.
            if i != len(text) - 1 and text[i] != text[i + 1]:
                l = nex[i + 1]
                if counts[text[i + 1]] > l:
                    ans = max(ans, 1 + l)
            if i != 0 and text[i] != text[i - 1]:
                l = pre[i - 1]
                if counts[text[i - 1]] > l:
                    ans = max(ans, 1 + l)
            if i != 0 and i != len(text) - 1 and text[i - 1] == text[i + 1]:
                # Match both forwards and backwards.
                l = pre[i - 1] + nex[i + 1]
                if counts[text[i - 1]] > l:
                    ans = max(ans, 1 + l)
                else:
                    # Can we still make it better?
                    ans = max(ans, l)
        return ans
            
        
            

