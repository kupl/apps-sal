class Solution:
    def clumsy(self, N: int) -> int:
        import functools
        l = list(reversed(list(range(1, N+1))))
        ll= list([z[1] for z in [x for x in enumerate(l) if x[0] %  4 == 0 or x[0] % 4 == 1 or x[0] % 4 == 2]])
        rs = sum(list([z[1] for z in [x for x in enumerate(l) if x[0] % 4 == 3]]))
        pr, acc = [], 1
        for( i, el) in enumerate(ll):
            if i % 3 == 0:acc = el
            elif i % 3 == 1:acc = acc * el
            else: acc = math.floor(acc / el)
            if i %3 == 2 or i == len(ll) -1:
                pr.append(acc)
        # print(l, ll, rs, pr)
        return rs + pr[0] + sum(list([-x for x in pr[1:]]))        

