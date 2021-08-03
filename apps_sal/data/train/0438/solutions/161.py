class Solution:

    def find(self, d, x):
        while x != d[x]:
            x = d[x]
        return x

    def union(self, d, x, y):
        px, py = self.find(d, x), self.find(d, y)
        if px != py:
            d[px] = py

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n, step = len(arr), -1
        s, d, d_len, d_rec = [0] * n, {i: i for i in range(n)}, [1] * n, dict()
        for i in range(n):
            num = arr[i] - 1
            s[num] = 1
            if num - 1 >= 0 and s[num - 1] == 1:
                temp = d_len[self.find(d, num - 1)]
                self.union(d, num - 1, num)
                d_rec[temp] -= 1
                d_len[num] += temp
            if num + 1 < n and s[num + 1] == 1:
                temp = d_len[self.find(d, num + 1)]
                self.union(d, num + 1, num)
                d_rec[temp] -= 1
                d_len[num] += temp
            d_rec[d_len[num]] = d_rec[d_len[num]] + 1 if d_len[num] in list(d_rec.keys()) else 1
            if m in list(d_rec.keys()) and d_rec[m] > 0:
                step = i + 1
        return step
