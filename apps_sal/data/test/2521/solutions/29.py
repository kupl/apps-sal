def main():
    n = int(input())
    a = list(map(int, input().split()))

    from heapq import heapify, heappushpop

    # first half
    fh = []
    l = a[:n]
    fh.append(sum(l))
    heapify(l)
    for i in a[n:2 * n]:
        if l[0] < i:
            fh.append(fh[-1] + i - heappushpop(l, i))
        else:
            fh.append(fh[-1])

    # latter half
    lh = []
    l = [-i for i in a[2 * n:]]
    lh.append(sum(l))
    heapify(l)
    for i in a[2 * n - 1:n - 1:-1]:
        if l[0] < -i:
            lh.append(lh[-1] - i - heappushpop(l, -i))
        else:
            lh.append(lh[-1])

    ans = fh[0] + lh[n]
    for i in range(1, n + 1):
        if ans < fh[i] + lh[n - i]:
            ans = fh[i] + lh[n - i]

    print(ans)


main()
