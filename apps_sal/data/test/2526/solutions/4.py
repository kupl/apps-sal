x_aka,y_mid,a,b,c = list(map(int,input().split()))
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
p_aka = sorted(p,reverse=True)
q_mid = sorted(q,reverse=True)
r_mu = sorted(r,reverse=True)
#print(p_aka[:x_aka],q_mid[:y_mid],r_mu)
tmp = p_aka[:x_aka] + q_mid[:y_mid] + r_mu
sort_tmp = sorted(tmp,reverse=True)
#print(sort_tmp[:(x_aka+y_mid)])
print((sum(sort_tmp[:(x_aka+y_mid)])))

