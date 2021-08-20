(A, B, C, D) = map(int, input().split())
print('Right' if C + D > A + B else 'Left' if C + D < A + B else 'Balanced')
