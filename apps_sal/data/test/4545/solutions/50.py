N = int(input())
A = int(input())
sum = N * N
if (1 <= N and N <= 100) and (0 <= A and A <= N ** N):
    print(sum - A)
