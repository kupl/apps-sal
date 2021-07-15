n = int(input())
a = list(map(int, input().split()))
a.sort(key=lambda x: -x)
s_p = sum([x for x in a if x > 0])
if s_p % 2 == 1:
    print(s_p)
else:
    m_p = list([x for x in a if x > 0 and x % 2 == 1])
    m_n = list([x for x in a if x < 0 and x % 2 == 1])    
    if len(m_p) > 0 and len(m_n) > 0:
        s_p += max(-min(m_p), max(m_n))
    elif len(m_p) == 0 and len(m_n) > 0:
        s_p += max(m_n)
    else:
        s_p += -min(m_p)
    print(s_p)


