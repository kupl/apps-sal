n, d = list(map(int, input().split()))
A = list(map(int, input().split()))
m = int(input())
if m < n:
    A = sorted(A)
    print(sum(A[:m]))
else:
    print(sum(A) - d * (m - n))
