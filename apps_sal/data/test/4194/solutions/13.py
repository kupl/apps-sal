N, M = map(int, input().split())
A = list(map(int, input().split()))

answer = N - sum(A)

if N >= sum(A):
    print(answer)

else:
    print('-1')
