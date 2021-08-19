def f(A):
    if len(A) == 1:
        return 1
    elif A == sorted(A):
        return len(A)
    else:
        return max(f(A[:len(A) // 2]), f(A[len(A) // 2:]))


n = int(input())
A = list(map(int, input().split()))
print(f(A))
