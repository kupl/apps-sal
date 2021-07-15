n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

m = (n + 1) // 2
if n % 2 == 0:
    print(sum(A[:m - 1]) + sum(A[1:m]) + A[m - 1])
else:
    print(sum(A[:m - 1]) + sum(A[1:m]))
