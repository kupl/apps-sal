class UnionFind:
    def __init__(self):
        self.rblong = dict()  # aRe BeLong to

    def find(self, n):
        if n not in self.rblong:
            self.rblong[n] = n
            return n

        if n == self.rblong[n]:
            return n

        self.rblong[n] = self.find(self.rblong[n])
        return self.rblong[n]

    def union(self, n1, n2):
        u1, u2 = self.find(n1), self.find(n2)
        if u1 == u2:
            return

        self.rblong[u1] = u2
        return


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind()
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]

        for num in A:
            if num == 1:
                continue

            num2 = num
            for i in prime:
                if num2 < i:
                    break

                if num2 % i == 0:
                    uf.union(num2, i)
                    num2 = num2 // i
                    if num2 > 1:
                        uf.union(num2, i)
                    while num2 % i == 0:
                        num2 = num2 // i
                        if num2 > 1:
                            uf.union(num2, i)

            if num2 > 1:
                uf.union(num, num2)

        # print(uf.rblong)
        count = dict()
        for num in A:
            tmp = uf.find(num)
            #print('num == {}, tmp == {}'.format(num, tmp))

            if tmp not in count:
                count[tmp] = 1

            else:
                count[tmp] += 1

        return max(count.values())
