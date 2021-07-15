class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import Counter
        counter = Counter(text)
        if not text: return 0
        if len(text) == 1: return 1
        def helper(text):
            start_idx, end_idx = 0, 0
            first_found = None
            ret = 0
            while end_idx < len(text):
                if text[end_idx] == text[start_idx]:
                    end_idx += 1
                    if counter[text[start_idx]] >= end_idx-start_idx:
                        ret = max(ret, end_idx-start_idx)
                    else:
                        ret = max(ret, end_idx-start_idx-1)
                else:
                    if not first_found:
                        first_found = end_idx
                        end_idx += 1 
                        if counter[text[start_idx]] >= end_idx-start_idx:
                            ret = max(ret, end_idx-start_idx)
                        else:
                            ret = max(ret, end_idx-start_idx-1)
                    else:
                        start_idx = end_idx = first_found
                        first_found = None
            return ret
        return max(helper(text), helper(text[::-1]))
