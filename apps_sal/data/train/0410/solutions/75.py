class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getSteps(lo):
            steps = 0
            reduced = lo
            while reduced != 1:
                if reduced % 2 == 0:
                    reduced = reduced / 2
                else:
                    reduced = 3*reduced+1
                steps += 1

            return (steps)


        a = {}
        for i in range(lo, hi+1):
            steps = getSteps(i)
            if steps not in a:
                a[steps] = [i]
            else:
                a[steps].append(i)

        r = []
        for key in sorted(a.keys()):
            for val in a[key]:
                r.append(val)

        return r[k-1]
