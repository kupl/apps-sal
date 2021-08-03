A = list(map(int, input().split()))

K = int(input())

A.sort(reverse=True)

print((A[0] * 2**K + A[1] + A[2]))
