(H, N) = map(int, input().split())
A = list(map(int, input().split()))
answer = sum(A)
if H <= answer:
    print('Yes')
else:
    print('No')
