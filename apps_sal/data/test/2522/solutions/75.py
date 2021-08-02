def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = [0] * (N + 1)
    for n in (A + B):
        cnt[n] += 1
    if max(cnt) > N:
        print('No')
        return
    # Bを逆順にすると、真ん中あたりで重複のペアが生じうる。そこを解消する。
    B = B[::-1]
    dup, dup_indices = -1, list()
    for i in range(N):
        if A[i] == B[i]:
            dup = A[i]
            dup_indices.append(i)
    if dup == -1:
        # 同じ数字のペアがないので、そのまま出力
        print('Yes')
        print(' '.join(map(str, B)))
        return
    # 真ん中あたりの重複ペア部分を他と入れ替える
    indices = list()
    for i in range(N):
        if A[i] != dup and B[i] != dup:
            indices.append(i)
    indices = indices[:len(dup_indices)]
    for i, j in zip(dup_indices, indices):
        B[i], B[j] = B[j], B[i]
    print('Yes')
    print(' '.join(map(str, B)))


def __starting_point():
    main()


__starting_point()
