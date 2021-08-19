def main():
    (N, M) = tuple([int(_x) for _x in input().split()])
    A = [int(_x) for _x in input().split()]
    total = sum(A)
    if total % (4 * M) == 0:
        min_vote = total // (4 * M)
    else:
        min_vote = 1 + total // (4 * M)
    cnt = 0
    for vot in A:
        if vot >= min_vote:
            cnt += 1
    if cnt >= M:
        print('Yes')
    else:
        print('No')


main()
