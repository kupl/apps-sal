class Solution:

    def find(self, d, x):
        while x != d[x]:
            x = d[x]
        return x

    def union(self, d, x, y):
        (px, py) = (self.find(d, x), self.find(d, y))
        if px != py:
            d[px] = py

    def findLatestStep(self, arr: List[int], m: int) -> int:
        (n, step, rec) = (len(arr), -1, 0)
        (s, d, d_len) = ([0] * n, {i: i for i in range(n)}, [1] * n)
        for i in range(n):
            num = arr[i] - 1
            s[num] = 1
            for j in (num - 1, num + 1):
                if j >= 0 and j < n and (s[j] == 1):
                    temp = d_len[self.find(d, j)]
                    if temp == m:
                        rec -= 1
                    self.union(d, j, num)
                    d_len[num] += temp
            if d_len[num] == m:
                rec += 1
            if rec > 0:
                step = i + 1
        return step
