class Solution(object):

    def maxLength(self, arr):

        def get_max_len(arr):
            dp = [set(x) for x in arr if len(set(x)) == len(x)]
            for v in arr:
                if len((a := set(v))) == len(v):
                    for b in dp:
                        if a & b:
                            continue
                        dp.append(a | b)
            return max((len(x) for x in dp)) if dp else 0
        return get_max_len(arr)
