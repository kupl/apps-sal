def solve():
    N = int(input())
    A = [-float('inf')] + list(map(int, input().split()))
    A.sort()
    ans = [A[-1]]
    n = A[-1] // 2
    for i in range(1, N + 1):
        if A[i] > n or i == N - 1:
            if A[i] - n > n - A[i - 1]:
                ans.append(A[i - 1])
            else:
                ans.append(A[i])
            break
    return ans


print(*solve())
