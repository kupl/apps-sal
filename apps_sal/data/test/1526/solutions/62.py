A = list(map(int, input().split()))
A.sort(reverse=True)
X = (A[0] - A[1]) + (A[0] - A[2])
if X % 2 == 0:
    print((X // 2))
else:
    print((X // 2 + 2))
