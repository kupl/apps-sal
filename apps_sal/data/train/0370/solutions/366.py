class Solution:
    def __init__(self):
        self.arr = []

    def fac(self, n):
        for i in range(2, floor(sqrt(n) + 1)):
            if n % i == 0:
                self.union(n, i)
                self.union(n, n // i)

    def find(self, x):
        if self.arr[x] != x:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.arr[xr] = yr

    def largestComponentSize(self, A: List[int]) -> int:

        self.arr = [0] * (max(A) + 1)
        ans = [0] * (max(A) + 1)
        A.sort()
        for j, i in enumerate(self.arr):
            self.arr[j] = j

        for i in A:
            self.fac(i)

        for i in A:
            ans[self.find(i)] += 1
        return max(ans)
