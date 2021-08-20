class Solution:

    def maxLength(self, arr: List[str]) -> int:
        d = ['']
        for a in arr:
            if len(set(a)) < len(a):
                continue
            else:
                for x in d:
                    if set(x) & set(a):
                        continue
                    else:
                        t = set(a) | set(x)
                        d.append(t)
        max = 0
        for i in d:
            if len(i) > max:
                max = len(i)
        return max
