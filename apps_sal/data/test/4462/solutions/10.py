N = int(input())
A = [int(a) for a in input().split(' ')]
m_2_but_4 = 0
m_4 = 0
m_none = 0
for i in range(len(A)):
    if A[i] % 4 == 0:
        m_4 += 1
    elif A[i] % 2 == 0:
        m_2_but_4 += 1
    else:
        m_none += 1
if m_2_but_4:
    print('Yes') if m_4 >= m_none else print('No')
else:
    print('Yes') if m_4 + 1 >= m_none else print('No')
