from sys import stdin
nii = lambda: map(int, stdin.readline().split())
lnii = lambda: list(map(int, stdin.readline().split()))

a, b, c = nii()
print('Yes' if a + b >= c else 'No')
