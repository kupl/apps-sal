N = int(input())
A = list(map(int, input().split()))

A = [0] + A + [0]
sum_all = 0

for i, a in enumerate(A[1:N + 2], start=1):
    sum_all += abs(a - A[i - 1])

for i, a in enumerate(A[1:N + 1], start=1):
    print((sum_all - abs(a - A[i - 1]) - abs(a - A[i + 1]) + abs(A[i + 1] - A[i - 1])))


