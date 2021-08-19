from collections import Counter


class Solution:
    def mul(self, x):
        ans = []
        n = len(x)
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans.append(x[i] * x[j])
        return ans

    def count(self, x, y):
        ans = 0
        cx = Counter(x)
        cy = Counter(y)
        same = set(x).intersection(set(y))
        for num in same:
            # print(num, cx, cy)
            ans += cx[num] * cy[num]
        return ans

    def numTriplets(self, a: List[int], b: List[int]) -> int:
        ans = 0
        asq = [i * i for i in a]
        bsq = [i * i for i in b]
        aa = self.mul(a)
        bb = self.mul(b)
        ans += self.count(asq, bb)
        ans += self.count(bsq, aa)
        return ans
