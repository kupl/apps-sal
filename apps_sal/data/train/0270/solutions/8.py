class Solution:

    def getHappyString(self, n: int, k: int) -> str:

        def stringformer(sts, prev):
            if len(sts) == n:
                l.append(sts)
                return
            for i in ['a', 'b', 'c']:
                if i != prev:
                    stringformer(sts + i, i)
        l = []
        stringformer('', '')
        if len(l) == 0 or k > len(l):
            return ''
        else:
            return l[k - 1]
