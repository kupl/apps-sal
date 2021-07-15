n = int(input())
M = 2 ** (n + 1)
A = [0, 0] + list(map(int, input().split()))
Ans = [0] * M
ans = 0
for i in range(2 ** n - 1, 0, -1):
    left = i * 2
    right = i * 2 + 1
    m_l = A[left] + Ans[left]
    m_r = A[right] + Ans[right]
    Ans[i] = max(m_l, m_r)
    ans += abs(m_l - m_r)
print(ans)


