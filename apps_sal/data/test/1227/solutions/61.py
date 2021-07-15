n=input()
k=int(input())

len_n=len(n)
dp0=[[0]*(k+1) for _ in range(len_n+1)]
dp1=[[0]*(k+1) for _ in range(len_n+1)]
dp0[0][0]=1
# dp0: N以下であることが未確定
# dp1: N以下であることが確定
for i, n_i in enumerate(n):
    for k_i in range(k+1):
        if n_i=='0':
            dp0[i+1][k_i]+=dp0[i][k_i]
            dp1[i+1][k_i]+=dp1[i][k_i]
            if k_i<k:
                dp1[i+1][k_i+1]+=9*dp1[i][k_i]
        else:
            if k_i<k:
                dp0[i+1][k_i+1]+=dp0[i][k_i]
                dp1[i+1][k_i+1]+=(int(n_i)-1)*dp0[i][k_i]
                dp1[i+1][k_i+1]+=9*dp1[i][k_i]
            dp1[i+1][k_i]+=dp0[i][k_i]
            dp1[i+1][k_i]+=dp1[i][k_i]

print((dp0[-1][k]+dp1[-1][k]))

