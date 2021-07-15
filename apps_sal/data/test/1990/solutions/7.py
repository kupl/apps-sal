'''input
11
(R)R(R)Ra)c
'''

# https://codeforces.com/blog/entry/18051
# Min = minimum prefix sum instead of minimum value

class SegmentTree:
    def __init__(self, n, arr=[]):
        self.n = n
        self.tsum = [0] * (2 * n)
        self.tmin = [0] * (2 * n)
        self.tmax = [0] * (2 * n)
        if arr:
            for i in range(len(arr)):
                self.tsum[n + i] = arr[i];
            for i in range(len(arr) - 1, 0, -1) :
                self.tsum[i] = self.tsum[i<<1] + self.tsum[i<<1|1];

    def update(self, p, val):
        p += self.n;
        self.tsum[p] = val;
        self.tmin[p] = val;
        self.tmax[p] = val;

        i = p;
        while i > 1:
            par = i>>1 # parent
            if i & 1: # i is a right child (odd index)
                self.tsum[par] = self.tsum[i] + self.tsum[i^1];
                self.tmin[par] = min(self.tmin[i^1], self.tmin[i] + self.tsum[i^1]) # i^1 = other child of i's parent
                self.tmax[par] = max(self.tmax[i^1], self.tmax[i] + self.tsum[i^1])
            else: # i is a left child
                self.tsum[par] = self.tsum[i] + self.tsum[i^1];
                self.tmin[par] = min(self.tmin[i], self.tmin[i^1] + self.tsum[i])
                self.tmax[par] = max(self.tmax[i], self.tmax[i^1] + self.tsum[i])
            i >>= 1;

'''
int query(int l, int r) {  // sum on interval [l, r)
  int res = 0;
  for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
    if (l&1) res += t[l++];
    if (r&1) res += t[--r];
  }
  return res;
}

'''

'''
import math
array = [1,3,5,7,9,11]
n = 2 ** math.ceil(math.log(len(array), 2))
st = SegmentTree(n, array)
st.update(0, 2)
'''

from sys import stdin
import math
def input():
    return stdin.readline()[:-1]

n = int(input())
s = input()

#n = 2 ** math.ceil(math.log(n, 2))
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

