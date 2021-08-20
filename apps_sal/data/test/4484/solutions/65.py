(n, m) = map(int, input().split())
mod = 10 ** 9 + 7
'\nabs(n-m)>1の時、必ず隣り合ってしまうので0\nn>mとしても一般性を失わない\nif n<m: n, m = m, n\nn==mnの時は、どちらを左端に置くか選べるので2倍\n'
if abs(n - m) > 1:
    print(0)
else:
    if n < m:
        (n, m) = (m, n)
    n_parm = 1
    for i in range(n, 0, -1):
        n_parm = n_parm * i % mod
    m_parm = 1
    for i in range(m, 0, -1):
        m_parm = m_parm * i % mod
    ans = n_parm * m_parm % mod
    if m == n:
        ans = ans * 2 % mod
    print(ans)
