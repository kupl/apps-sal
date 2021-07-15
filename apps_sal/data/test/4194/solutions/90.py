N, M = map(int, input().split())
A = list(map(int, input().split()))
a_sum = sum(A)

if N - a_sum >= 0:
    print(N - a_sum)
else:
    print('-1')
