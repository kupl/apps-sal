(A, B, C, D) = map(int, input().split())
高 = -(-C // B)
青 = -(-A // D)
if 高 <= 青:
    print('Yes')
else:
    print('No')
