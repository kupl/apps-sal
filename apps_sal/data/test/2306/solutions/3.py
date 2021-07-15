def calc_vt(v,t):
    vt = [0]*(sum(t)*2+1)
    t_sum = 0
    for ti,vi in zip(t,v):
        for i in range(ti*2):
            vt[t_sum + 1 + i] = min(vt[t_sum + i] + 0.5,vi)
        t_sum += ti*2
    return vt

n = input().split()
tn = list(map(int,input().split()))
vn = list(map(int,input().split()))

vt_l = calc_vt(vn,tn)
vt_r = calc_vt(vn[::-1],tn[::-1])[::-1]

vt_lr = [min(vl,vr) for vl,vr in zip(vt_l,vt_r)]

print((sum((a+b)*0.5/2 for a,b in zip(vt_lr,vt_lr[1:]))))

