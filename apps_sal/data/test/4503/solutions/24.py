(H, N) = map(int, input().split())
A = map(int, input().split())
a_sum = sum(A)
if H - a_sum <= 0:
    print('Yes')
else:
    print('No')
