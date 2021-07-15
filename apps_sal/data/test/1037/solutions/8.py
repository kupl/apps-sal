e=enumerate
n,a=open(0)
n=int(n)
d=[0]
for j,(a,i)in e(sorted((int(a),i)for i,a in e(a.split()))[::-1]):d=[d[0]+a*(~i-j+n)]+[max(d[k+1]+a*(n+k-i-j),t+a*abs(i-k))for k,t in e(d[:j])]+[d[j]+a*abs(i-j)]
print(max(d))
