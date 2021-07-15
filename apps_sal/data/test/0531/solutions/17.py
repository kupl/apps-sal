n = int(input())
x = n*[0]
s = input().split()
for i in range(n):
    x[i] = int(s[i])
m = min(x)
M = max(x)

if (M-m < 2):
    print(n)
    for e in x:
        print(e, end=" ")
else:
    m_num = 0
    M_num = 0
    for e in x:
        if e==m:
            m_num += 1
        elif e==M:
            M_num += 1
    mid_num = n-m_num-M_num

    candidate_min1 = 0
    if mid_num%2 == 0:
        candidate_min1 = m_num+M_num
    else:
        candidate_min1 = m_num+M_num+1

    candidate_min2 = mid_num+abs(m_num-M_num)

    if candidate_min1 <= candidate_min2:
        print(candidate_min1)
        if mid_num%2 == 0:
            for i in range(int(m_num+mid_num/2)):
                print(m, end=" ")
            for i in range(int(M_num+mid_num/2)):
                print(M, end=" ")
        else:
            for i in range(int(m_num+(mid_num-1)/2)):
                print(m, end=" ")
            print(m+1, end=" ")
            for i in range(int(M_num+(mid_num-1)/2)):
                print(M, end=" ")

    else:
        print(candidate_min2)
        if M_num-m_num >= 0:
            for i in range(M_num-m_num):
                print (M, end=" ")
            for i in range(n-(M_num-m_num)):
                print (M-1, end=" ")
            
        elif M_num-m_num < 0:
            for i in range(m_num-M_num):
                print (m, end=" ")
            for i in range(n-(m_num-M_num)):
                print (m+1, end=" ")


    


