(A, B, C, D) = map(int, input().split())
while A > 0 and C > 0:
    C -= B
    A -= D
if C <= 0:
    print('Yes')
else:
    print('No')
