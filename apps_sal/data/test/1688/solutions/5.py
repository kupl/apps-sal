import sys
input = sys.stdin.readline


class SegTree(object):
    """docstring for SegTree"""

    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.tree = [0 for i in range(2 * n)]

    def construct(self):  # Construction
        for i in range(self.n):
            self.tree[n + i] = self.arr[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.function(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, change):
        start = index + self.n
        self.tree[start] = value
        while start > 0:
            self.tree[start] = self.function(self.tree[2 * start], self.tree[2 * start + 1])
            start = start // 2

    def calc(self, low, high):  # 0-indexed
        low += self.n
        high += self.n
        ans = 0  # Needs to initialised
        while low < high:
            if low % 2:
                ans = self.function(ans, self.tree[low])
                low += 1
            if high % 2:
                high -= 1
                ans = self.function(ans, self.tree[high])
            low = low // 2
            high = high // 2
        return ans

    def function(self, a, b):  # Function used to construct Segment Tree
        return max(a, b)


n = int(input()) * 3
a = list(map(int, input().split()))
a = a + a + a
st = SegTree(n, a)
st.construct()
ans = [-1] * n
m = a[0]
flag = 0
for i in range(1, n):
    if a[i] <= (m - 1) // 2:
        ans[0] = i
        flag = 1
        prev = i
        break
    else:
        m = max(m, a[i])
if not flag:
    print(*ans[0:n // 3])
    return
for i in range(1, n // 3):
    if a[i] >= a[i - 1]:
        ans[i] = ans[i - 1] - 1
    else:
        maxx = st.calc(i, prev + 1)
        while a[prev] > (maxx - 1) // 2:
            # print (prev,i,maxx)
            maxx = max(maxx, a[prev])
            prev += 1
        ans[i] = prev - i
print(*ans[0:n // 3])
