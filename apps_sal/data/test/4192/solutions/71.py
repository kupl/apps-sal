from sys import stdin
(D, T, S) = [int(_) for _ in stdin.readline().rstrip().split()]
if D / S <= T:
    print('Yes')
else:
    print('No')
