N=int(input())
A=list(map(int,input().split()))
import numpy as np
A_np=np.array(A)
data=np.array(list(range(1,N+1)))
A_i=sorted(A_np-data)
if N%2==0:
    x=A_i[int(N/2)-1]
    y=A_i[int(N/2)]
    A_x=A_i-x
    A_p_x=A_x[(A_x>=0)]
    A_m_x=A_x[(A_x<0)]
    A_y=A_i-y
    A_p_y=A_y[(A_y>=0)]
    A_m_y=A_y[(A_y<0)]
    ans=min(sum(A_p_x)-sum(A_m_x),sum(A_p_y)-sum(A_m_y))
    print(ans)
else:
    x=A_i[int((N-1)/2)]
    A_x=A_i-x
    A_p=A_x[(A_x>=0)]
    A_m=A_x[(A_x<0)]
    ans=sum(A_p)-sum(A_m)
    print(ans)
