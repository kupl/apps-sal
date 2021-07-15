from bisect import bisect_left

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    L, R = 0, 2 * 10**5 + 1
    while L+1 < R:
        P = (L+R)//2
        cnt = 0
        for v in a:
            x = P - v
            cnt += n - bisect_left(a, x)
        if cnt >= m:
            L = P
        else:
            R = P
    csum = [0]
    for v in a:
        csum.append(v)
    for i in range(n):
        csum[i+1] += csum[i]
    ans = 0
    cnt = 0
    for v in a:
        x = L - v
        idx = bisect_left(a, x)
        cnt += n-idx
        ans += csum[-1] - csum[idx]
        ans += v * (n - idx)
    ans -= (cnt - m) * L
    print(ans)

def __starting_point():
    main()
__starting_point()
