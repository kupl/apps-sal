class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        ret = list(s)

        while True:
            s = ret
            ret = []
            ac = 1
            for c in s:
                if not ret or ret[-1] != c:
                    ac = 1
                    ret.append(c)
                else:
                    if ac + 1 == k:
                        while ac:
                            ret.pop()
                            ac -= 1
                    else:
                        ret.append(c)
                        ac += 1
            if len(ret) == len(s):
                break

        return ''.join(ret)
