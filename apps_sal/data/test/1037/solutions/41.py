e=enumerate
n,a=open(0)
n=int(n)
d=[0]+[-2**64]*n
for j,(a,i)in e(sorted((-int(a),i)for i,a in e(a.split()))):d=[max(t-a*(~i-j+k+n),d[k-1]-a*abs(~i+k))for k,t in e(d)]
print(max(d))
