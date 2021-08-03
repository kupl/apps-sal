from bisect import bisect_right


def answer(n, A):
    ans = [A[0]]
    for i in range(1, n):
        if ans[-1] < A[i]:
            ans.append(A[i])
        else:
            index = bisect_right(ans, A[i])
            ans[index] = A[i]

    return len(ans)


n = int(input())
arr = list(map(int, input().split()))
print(answer(n, arr))
