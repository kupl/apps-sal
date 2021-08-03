n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_ = 0
max_ += min(A[0], B[1])
max_ += min(A[1], B[2])
max_ += min(A[2], B[0])


min_ = 0
min_ += max(0, A[0] - B[0] - B[2])
min_ += max(0, A[1] - B[0] - B[1])
min_ += max(0, A[2] - B[1] - B[2])

print(min_, max_)
