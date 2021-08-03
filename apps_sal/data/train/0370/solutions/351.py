class unionfind:
    def __init__(self, N):
        self.parents = list(range(N))
        self.size = [1] * N

    def find(self, x):
        while x != self.parents[x]:
            x = self.parents[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            sizex, sizey = self.size[px], self.size[py]
            if sizex < sizey:
                self.parents[px] = py
                self.size[py] += sizex
            else:
                self.parents[py] = px
                self.size[px] += sizey
        else:
            return


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        factor_dic = collections.defaultdict(int)
        uf = unionfind(len(A))
        for idx, a in enumerate(A):
            for factor in range(2, int(a**0.5) + 1):
                if a % factor == 0:
                    for fac in [factor, a // factor]:
                        if fac not in factor_dic:
                            factor_dic[fac] = idx
                        else:
                            # if idx == 2:
                            #     print(idx, fac)
                            #     print(factor_dic)
                            uf.union(idx, factor_dic[fac])
            if a not in factor_dic:
                factor_dic[a] = idx
            else:
                uf.union(idx, factor_dic[a])
        # print(factor_dic)
        # print(uf.parents)
        # print(uf.size)
        return max(uf.size)
