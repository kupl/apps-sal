def main():
    n = int(input())
    height = [] 
    width = []
    for i in range(n):
        a, b = map(int, input().split())
        width.append(a)
        height.append(b)
    s_w = sum(width)
    m_h = max(height)
    a = height.index(m_h)
    height[a] = 0
    s_m = max(height)
    height[a] = m_h
    for i in range(n):
        if height[i] != m_h:
            print((s_w -width[i]) * m_h, end=' ')
        else:
            print(s_m * (s_w -width[i]), end=' ')
main()
