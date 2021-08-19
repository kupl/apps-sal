from math import gcd
for _ in range(int(input())):
    n = int(input())
    p2 = list(map(int, input().split()))
    p = sorted(p2, reverse=True)
    (x, a) = list(map(int, input().split()))
    (y, b) = list(map(int, input().split()))
    k = int(input())
    l = -1
    r = n + 1
    while r - l > 1:
        mid = (r + l) // 2
        m_cnt3 = mid // (a * b // gcd(a, b))
        m_cnt1 = mid // a - m_cnt3
        m_cnt2 = mid // b - m_cnt3
        res = sum(p[:m_cnt3]) // 100 * (x + y)
        if x > y:
            res += sum(p[m_cnt3:m_cnt1 + m_cnt3]) // 100 * x + sum(p[m_cnt1 + m_cnt3:m_cnt1 + m_cnt2 + m_cnt3]) // 100 * y
        else:
            res += sum(p[m_cnt3:m_cnt2 + m_cnt3]) // 100 * y + sum(p[m_cnt2 + m_cnt3:m_cnt1 + m_cnt2 + m_cnt3]) // 100 * x
        if res < k:
            l = mid
        else:
            r = mid
    if r == n + 1:
        print(-1)
    else:
        print(r)
