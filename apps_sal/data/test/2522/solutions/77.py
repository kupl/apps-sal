def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.reverse()
    (l, r) = (0, N - 1)
    for i in range(N):
        if A[i] != B[i]:
            continue
        if l < i and A[i] != B[l] and (A[l] != B[i]):
            (B[l], B[i]) = (B[i], B[l])
            l += 1
            continue
        if i < r and A[i] != B[r]:
            (B[i], B[r]) = (B[r], B[i])
            r -= 1
            continue
        return None
    return B


t = main()
if t is None:
    print('No')
else:
    print('Yes')
    print(' '.join(map(str, t)))
