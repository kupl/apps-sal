(A, B, C, N) = [int(i) for i in input().split()]
count = A + B - C
if C > A or C > B:
    print(-1)
elif count < 0:
    print(-1)
elif count >= N:
    print(-1)
else:
    print(N - count)
