H, N = map(int, input().split())
A = list(map(int, input().split()))
A1 = sum(A)

if H - A1 <= 0:
    print('Yes')
else:
    print('No')
