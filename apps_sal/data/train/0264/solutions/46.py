class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ret = [set()]

        for string in arr:
            curr = set(string)
            if len(curr) == len(string):
                for seen in ret:
                    if not (seen & curr):
                        ret.append(seen | curr)
        max_len = 0
        for string in ret:
            max_len = max(max_len, len(string))
        return max_len
