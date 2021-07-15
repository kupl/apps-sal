n=int(input())
p=list(map(int,input().split()))
l=[0]+[i for i in range(n+1)]#l_i...p_iよりも大きいもので、左側かつp_iに一番近い要素のindex
r=[i+1 for i in range(n+1)]+[n+1]#r_i...l_iの右側ver
d=[0]*(n+1)
for i in range(n):d[p[i]]=i+1
ans=0
for i in range(1,n+1):
  ans+=((r[r[d[i]]]-r[d[i]])*(d[i]-l[d[i]])+(r[d[i]]-d[i])*(l[d[i]]-l[l[d[i]]]))*i#l_iでで一番近い、l_(l_i)で二番目に近い(indexの差分取ってアレコレ計算)
  l[r[d[i]]],r[l[d[i]]]=l[d[i]],r[d[i]]#右側(左側)にある一番近いものを、自分を飛び越えて左側(右側)にくっつける(大小比較はしなくても良くて、どうせ後でまた更新される)
print(ans)
