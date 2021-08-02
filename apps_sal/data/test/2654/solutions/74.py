n = int(input())
A, B = map(list, zip(*[map(int, input().split()) for i in range(n)]))
A.sort()
B.sort()
if n & 1:
    print(B[n // 2] - A[n // 2] + 1)
else:
    print(B[n // 2] + B[n // 2 - 1] - (A[n // 2] + A[n // 2 - 1]) + 1)
