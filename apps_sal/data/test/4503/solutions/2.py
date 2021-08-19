(H, N) = list(map(int, input().split()))
A = list(map(int, input().split()))
print('Yes' if H - sum(A) <= 0 else 'No')
