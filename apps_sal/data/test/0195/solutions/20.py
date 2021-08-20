(A, B, C, N) = [int(i) for i in input().split()]
summ = A - C + B
if summ >= N or C > min(A, B):
    print(-1)
else:
    print(N - summ)
