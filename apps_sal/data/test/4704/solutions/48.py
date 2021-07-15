n = int(input())
A = list(map(int, input().split()))

s = A[0]
s_ = sum(A[1:])
gap = abs(s-s_)
for i in range(1, n-1):
    s += A[i]
    s_ -= A[i]
    if gap > abs(s-s_):
        gap = abs(s-s_)
print(gap)
