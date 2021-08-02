from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


a, b, c, d = nii()
if (abs(a - b) <= d and abs(c - b) <= d) or abs(c - a) <= d:
    print('Yes')
else:
    print('No')
