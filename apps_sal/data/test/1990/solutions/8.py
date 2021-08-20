"""input
11
(R)R(R)Ra)c
"""
from sys import stdin


class SegmentTree:

    def __init__(self, n, arr=[]):
        self.n = n
        self.tsum = [0] * (2 * n)
        self.tmin = [0] * (2 * n)
        self.tmax = [0] * (2 * n)
        if arr:
            for i in range(len(arr)):
                self.tsum[n + i] = arr[i]
            for i in range(len(arr) - 1, 0, -1):
                self.tsum[i] = self.tsum[i << 1] + self.tsum[i << 1 | 1]

    def update(self, p, val):
        p += self.n
        self.tsum[p] = val
        self.tmin[p] = val
        self.tmax[p] = val
        i = p
        while i > 1:
            par = i >> 1
            if i & 1:
                self.tsum[par] = self.tsum[i] + self.tsum[i ^ 1]
                self.tmin[par] = min(self.tmin[i ^ 1], self.tmin[i] + self.tsum[i ^ 1])
                self.tmax[par] = max(self.tmax[i ^ 1], self.tmax[i] + self.tsum[i ^ 1])
            else:
                self.tsum[par] = self.tsum[i] + self.tsum[i ^ 1]
                self.tmin[par] = min(self.tmin[i], self.tmin[i ^ 1] + self.tsum[i])
                self.tmax[par] = max(self.tmax[i], self.tmax[i ^ 1] + self.tsum[i])
            i >>= 1


'\nint query(int l, int r) {  // sum on interval [l, r)\n  int res = 0;\n  for (l += n, r += n; l < r; l >>= 1, r >>= 1) {\n    if (l&1) res += t[l++];\n    if (r&1) res += t[--r];\n  }\n  return res;\n}\n\n'
'\nimport math\narray = [1,3,5,7,9,11]\nn = 2 ** math.ceil(math.log(len(array), 2))\nst = SegmentTree(n, array)\nst.update(0, 2)\n'


def input():
    return stdin.readline()[:-1]


def main():
    n = int(input())
    s = input()
    n = 1048576
    st = SegmentTree(n)
    maxit = -1
    currentit = 0
    output = []
    for c in s:
        if c == 'L':
            currentit = max(0, currentit - 1)
        elif c == 'R':
            currentit += 1
        else:
            maxit = max(maxit, currentit)
            if c == '(':
                st.update(currentit, 1)
            elif c == ')':
                st.update(currentit, -1)
            else:
                st.update(currentit, 0)
        vmax = st.tmax[1]
        vmin = st.tmin[1]
        vsum = st.tsum[1]
        if vmin >= 0 and vsum == 0:
            output.append(vmax)
        else:
            output.append(-1)
    print(' '.join(map(str, output)))


def __starting_point():
    main()


__starting_point()
