def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = [0] * (N + 1)
    for n in A + B:
        cnt[n] += 1
    if max(cnt) > N:
        print('No')
        return
    B = B[::-1]
    (dup, dup_indices) = (-1, list())
    for i in range(N):
        if A[i] == B[i]:
            dup = A[i]
            dup_indices.append(i)
    if dup == -1:
        print('Yes')
        print(' '.join(map(str, B)))
        return
    indices = list()
    for i in range(N):
        if A[i] != dup and B[i] != dup:
            indices.append(i)
    indices = indices[:len(dup_indices)]
    for (i, j) in zip(dup_indices, indices):
        (B[i], B[j]) = (B[j], B[i])
    print('Yes')
    print(' '.join(map(str, B)))


def __starting_point():
    main()


__starting_point()
