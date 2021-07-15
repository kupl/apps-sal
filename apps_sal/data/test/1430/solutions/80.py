N,K = list(map(int,input().split()))
S = list(input())

S_zero={}
S_zero_group = 0
s_befor = ''
for s_idx,s in enumerate(S):
    if s != s_befor:
        if s == '0':
            S_zero_group += 1
            S_zero[S_zero_group] = [s_idx-1]
        elif s == '1':
            if S_zero_group in S_zero.keys():
                S_zero[S_zero_group].append(s_idx)
            
    s_befor = s
    
if S[-1] == '0':
    S_zero[S_zero_group].append(N)
    
if S_zero_group <= K:
    ans_ = N
else:   
    ans_=0
    for g_s in range(1,S_zero_group-K+2):
        g_e = g_s + K - 1
#         print('====',g_s,g_e)
        s = 0
        e = N-1

        if g_s != 1:
            s = S_zero[g_s-1][1]
        if g_e != S_zero_group:
            e = S_zero[g_e+1][0]

        ans= e-s+1
        if ans > ans_:
            ans_=ans

print(ans_)
