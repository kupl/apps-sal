import sys
input = sys.stdin.readline  # for speed up
sys.setrecursionlimit(10**7)

n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aa = [0] * (len(a) + 1)
bb = [0] * (len(b) + 1)

for ii in range(len(a)):
    aa[ii + 1] = aa[ii] + a[ii]
for ii in range(len(b)):
    bb[ii + 1] = bb[ii] + b[ii]

ii = 0
jmax = 0
r = 0
for jj in range(len(aa)):
    if aa[jj] > k:
        break
    else:
        r = ii + jj
        jmax = jj

for ii in range(len(bb)):
    for jj in range(jmax, -1, -1):
        if bb[ii] > k - aa[jj]:
            pass
        else:
            jmax = jj
            r = max(r, ii + jj)
            break
"""
for ii in range(m+1):
  print(c[ii])
"""

print(r)
