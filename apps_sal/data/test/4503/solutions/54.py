(H, N) = list(map(int, input().split()))
S = sum(list(map(int, input().split())))
if H <= S:
    print('Yes')
else:
    print('No')
