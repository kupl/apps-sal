# 4つのおもりで天秤の重さ比べ

A, B, C, D = map(int, input().split())
L = A + B
R = C + D

if L > R:
    print('Left')
elif L == R:
    print('Balanced')
else:
    print('Right')
