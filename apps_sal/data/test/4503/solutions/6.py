(H, N) = list(map(int, input().split()))
A = list(map(int, input().split()))
a_sum = sum(A)
if sum(A) - H >= 0:
    print('Yes')
else:
    print('No')
