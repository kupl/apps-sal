(h2, m2) = list(map(int, input().split(':')))
(h_sleep, m_sleep) = list(map(int, input().split(':')))
t2 = m2 + h2 * 60
t_sleep = m_sleep + h_sleep * 60
t2 -= t_sleep
if t2 < 0:
    t2 += 60 * 24
print('0' * (2 - len(str(t2 // 60))) + str(t2 // 60) + ':' + '0' * (2 - len(str(t2 % 60))) + str(t2 % 60))
