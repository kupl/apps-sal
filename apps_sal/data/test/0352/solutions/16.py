n = int(input())
(m_1, mx_1) = list(map(int, input().split()))
(m_2, mx_2) = list(map(int, input().split()))
(m_3, mx_3) = list(map(int, input().split()))
ans = [m_1, m_2, m_3]
s = sum(ans)
if s == n:
    print(*ans)
else:
    ans[0] += min(n - s, mx_1 - m_1)
    if ans[0] == mx_1:
        s += mx_1 - m_1
        ans[1] += min(n - s, mx_2 - m_2)
        if ans[1] == mx_2:
            s += mx_2 - m_2
            ans[2] += min(n - s, mx_3 - m_3)
    print(*ans)
