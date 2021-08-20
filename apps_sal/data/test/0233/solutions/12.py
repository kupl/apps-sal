n = int(input())
m_win = 0
c_win = 0
for i in range(n):
    (m, c) = list(map(int, input().split()))
    if m > c:
        m_win += 1
    if c > m:
        c_win += 1
if m_win > c_win:
    print('Mishka')
elif c_win > m_win:
    print('Chris')
else:
    print('Friendship is magic!^^')
