N = int(input())
A = list(map(int, input().split()))


def longest(A):
    if A == sorted(A):
        return len(A)
    return max(longest(A[:len(A) // 2]), longest(A[len(A) // 2:]))


print(longest(A))
