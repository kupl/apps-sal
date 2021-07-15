L,A,B,M=map(int,input().split())
MOD=M

#n*n行列の積を繰り返し二乗法で求める
#単位行列
def imat(n):
  ret=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
  return ret

#行列の積A*B
def prod_mat(amat,bmat):
  res_mat = [[sum([amat[i][j]*bmat[j][k] for j in range(len(bmat))]) for k in range(len(bmat[0]))] for i in range(len(amat))]
  return res_mat  

def powmod_mat(amat,p):
  if p==0:
    return imat(len(amat))
  else:
    pow2=powmod_mat(amat,p//2)
    if p%2==0:
      res_mat=prod_mat(pow2,pow2)
    else:
      res_mat=prod_mat(amat,prod_mat(pow2,pow2))

    for i in range(len(amat)):
      for j in range(len(amat)):
        res_mat[i][j]%=MOD
    return res_mat

slist=[]
for d in range(1,19):
  s=-(-(10**d-A)//B)
  if s>=0:
    slist.append(min(s,L))
  else:
    slist.append(0)
#print(slist)

dlist=[slist[0]]
for d in range(1,18):
  dlist.append(slist[d]-slist[d-1])
#print(dlist)

mat=imat(3)
for d in range(18):
  e=dlist[d]
  pmat=powmod_mat([[10**(d+1),1,0],[0,1,B],[0,0,1]],e)
  mat=prod_mat(pmat,mat)
  for i in range(3):
    for j in range(3):
      mat[i][j]%=MOD

#init
vec=[[0],[A],[1]]
vec=prod_mat(mat,vec)
print(vec[0][0]%MOD)
