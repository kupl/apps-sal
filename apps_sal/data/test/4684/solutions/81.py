(r, g, b) = list(map(int, input().split()))
N = r * 100 + g * 10 + b
if N % 4 == 0:
    print('YES')
else:
    print('NO')
