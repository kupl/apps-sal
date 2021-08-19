(A, B, C, D) = list(map(int, input().split()))
m = C // B
if C % B != 0:
    m = m + 1
n = A // D
if A % D != 0:
    n = n + 1
if n >= m:
    print('Yes')
else:
    print('No')
