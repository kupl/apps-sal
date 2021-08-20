(A, B, C) = map(int, input().split())
while B != 0:
    (A, B) = (B, A % B)
print('YES' if C % A == 0 else 'NO')
