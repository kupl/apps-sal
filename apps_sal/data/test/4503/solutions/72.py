H, N = map(int, input().split())
A = list(map(int, input().split()))

answer = sum(A)

if answer >= H:
    print('Yes')
else:
    print('No')
