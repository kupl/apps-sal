def main():
    from heapq import heappush, heappop
    from operator import itemgetter
    import sys
    input = sys.stdin.readline
    (N, K) = list(map(int, input().split()))
    dd = []
    for _ in range(N):
        (t, d) = list(map(int, input().split()))
        t -= 1
        dd.append((d, t))
    dd.sort(key=itemgetter(0), reverse=True)
    ret = 0
    biggest = [-1] * N
    h = []
    kinds = 0
    for (d, t) in dd[:K]:
        ret += d
        if ~biggest[t]:
            if biggest[t] > d:
                heappush(h, d)
            else:
                heappush(h, biggest[t])
                biggest[t] = d
        else:
            kinds += 1
            ret += kinds * 2 - 1
            biggest[t] = d
    ans = ret
    for (d, t) in dd[K:]:
        if ~biggest[t]:
            continue
        if not h:
            break
        kinds += 1
        diff = d + kinds * 2 - 1 - h[0]
        ret += diff
        if ans < ret:
            ans = ret
        biggest[t] = d
        heappop(h)
    print(ans)


def __starting_point():
    main()


__starting_point()
