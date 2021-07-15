class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # out
        tcounter = Counter(text)
        res = 0
        counter = Counter()
        i = 0
        for j in range(len(text)):
            counter[text[j]] += 1
            
            while j-i+1-max(counter.values())>1:
                counter[text[i]] -= 1
                i += 1
            
            curr_max = max(counter.values())
            c = [k for k in counter if counter[k]==curr_max][0]
            res = max(res, min(j-i+1, tcounter[c]))
            
        return res
