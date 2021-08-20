(H, N) = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)
if s >= H:
    print('Yes')
else:
    print('No')
