from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


a, b, c = nii()
print('Yes' if a + b >= c else 'No')
