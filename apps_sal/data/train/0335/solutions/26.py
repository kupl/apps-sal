class Solution(object):
    def tallestBillboard(self, rods):
        def make(A):
            states = {(0, 0)}
            for x in A:
                states |= ({(a+x, b) for a, b in states} |
                           {(a, b+x) for a, b in states})

            delta = {}
            for a, b in states:
                delta[a-b] = max(delta.get(a-b, 0), a)
            return delta

        N = len(rods)
        Ldelta = make(rods[:N//2])
        Rdelta = make(rods[N//2:])

        ans = 0
        for d in Ldelta:
            if -d in Rdelta:
                ans = max(ans, Ldelta[d] + Rdelta[-d])
        return ans
