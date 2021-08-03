def main():
    def solve2():
        a = m[:]
        cnt = 0
        t = 1 if Sum % n else 0
        while max(a) - min(a) != t:
            mn = a.index(min(a))
            mx = a.index(max(a))
            a[mn] += 1
            a[mx] -= 1
            cnt += 1
        return cnt
    n = int(input())
    m = list(map(int, input().split()))
    Sum = sum(m)
    mid = Sum // n
    if Sum % n == 0:
        ans = sum(abs(i - mid) for i in m) // 2
    else:
        cntscd = Sum % n
        cnt = ans = 0
        for i in m:
            if i > mid and cnt < cntscd:
                cnt += 1
                ans += i - mid - 1
            else:
                ans += abs(mid - i)
        ans += cntscd - cnt
        ans = ans // 2
    print(ans)


main()
