x = int(input())

h, m = [int(x) for x in input().split()]

for y in range(3600):
    t = h * 60 + m - x * y
    if t < 0:
        t += 60 * 24
    h_new = t // 60
    m_new = t % 60
    
    if '7' in str(h_new) + str(m_new):
        print(y)
        break

