class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def split(s):
            if not s:
                return [set()]
            n = len(s)

            w = set()
            w.add(tuple([s]))

            ret = [set([s])]
            if n == 1:
                return ret
            if n == 2:
                if s[0] != s[1]:
                    ret += [set([*s])]
                return ret
            for i in range(1, n):
                ls = split(s[0:i])
                rs = split(s[i:n])
                for l in ls:
                    for r in rs:
                        if len(l.intersection(r)) == 0:
                            e = tuple(sorted(list(l | r)))
                            if e not in w:
                                w.add(e)
                                ret += [l | r]
            return ret

        if not s:
            return 0
        n = len(s)
        if n < 10:
            ws = split(s)
            return max(map(len, ws))
        else:
            ans = 0

            ls = split(s[:7])
            rs = split(s[7:])
            ws = []
            w = set()
            for l in ls:
                for r in rs:
                    if len(l.intersection(r)) == 0:
                        e = tuple(sorted(list(l | r)))
                        if e not in w:
                            w.add(e)
                            ws += [l | r]
            ans = max(ans, max(map(len, ws)))

            ls = split(s[:6])
            rs = split(s[6:])
            ws = []
            w = set()
            for l in ls:
                for r in rs:
                    if len(l.intersection(r)) == 0:
                        e = tuple(sorted(list(l | r)))
                        if e not in w:
                            w.add(e)
                            ws += [l | r]
            ans = max(ans, max(map(len, ws)))

            return ans
