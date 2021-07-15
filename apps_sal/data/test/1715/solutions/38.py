import bisect
A,B,Q =list(map(int,input().split()))
s = []
t = []
for i in range(A):
    s.append(int(input()))
for i in range(B):
    t.append(int(input()))
for i in range(Q):
    x=(int(input()))    
    s_index_af = bisect.bisect(s,x)
    if s_index_af == A:
        s_index_af -= 1
        s_index_bf = s_index_af
    else:
        s_index_bf = s_index_af -1

    t_index_af = bisect.bisect(t,x)
    if t_index_af == B:
        t_index_af -= 1
        t_index_bf = t_index_af
    else:
        t_index_bf = t_index_af -1
   
    jl = [s[s_index_bf]-x,s[s_index_af]-x]
    tl = [t[t_index_bf]-x,t[t_index_af]-x]

    jt = []
    jt.append(abs(jl[0])+abs(tl[0]-jl[0]))
    jt.append(abs(jl[0])+abs(tl[1]-jl[0]))
    jt.append(abs(jl[1])+abs(tl[0]-jl[1]))
    jt.append(abs(jl[1])+abs(tl[1]-jl[1]))

    jt.append(abs(tl[0])+abs(jl[0]-tl[0]))
    jt.append(abs(tl[0])+abs(jl[1]-tl[0]))
    jt.append(abs(tl[1])+abs(jl[0]-tl[1]))
    jt.append(abs(tl[1])+abs(jl[1]-tl[1]))

            
    print((min(jt)))

