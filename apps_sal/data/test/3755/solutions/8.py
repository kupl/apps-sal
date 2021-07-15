
def main1(n,a):
  # n個の数字。パターン1の操作で1個減る。パターン2の操作で2個減る
  # n<=2000
  # パターン1だけするとき。max(a)が最大
  # パターン2を1回するとき。max(a)かmax(a[i]+a[i+2])が最大
  # パターン2を2回するとき。max(a)かmax(a[i]+a[i+2])かmax(a[i]+a[i+4])かmax(a[i]+a[i+2]+a[i+4])が最大
  # パターン2を3回するとき。max(a[i]+a[i+6])かmax(a[i]+a[i+4]+a[i+6])max(a[i]+a[i+2]+a[i+6])かmax(a[i]+a[i+2]+a[i+4]+a[i+6])が最大
  # 偶奇が異なるidxの要素が足されることがあるか？　ない
  # idx奇数の部分和で最大、つまり、負以外すべて足す。これを偶数でもする
  odary=[]
  odnum=0
  evary=[]
  evnum=0
  for i,x in enumerate(a):
    if x<=0:continue
    if i%2==0:
      evary.append(i)
      evnum+=x
    else:
      odary.append(i)
      odnum+=x
  if odnum==0 and evnum==0:
    mv,mi=a[0],0
    for i,x in enumerate(a):
      if mv<x:
        mv=x
        mi=i
    ret=mv
    ary=[mi]
  elif odnum>evnum:
    ret=odnum
    ary=odary
  else:
    ret=evnum
    ary=evary 
  retary=[]
  m=n
  #print(ary)
  for i in reversed(range(len(ary)-1)):
    t=ary[i+1]-ary[i]
    t//=2
    for j in range(t):
      retary.append((ary[i+1]+ary[i])//2-j+1)
      m-=2
  for _ in range(ary[0]):
    retary.append(1)
    m-=1
  for _ in range(n-1-ary[-1]):
    retary.append(m)
    m-=1
  return ret,retary

def __starting_point():
  n=int(input())
  a=list(map(int,input().split()))
  ret1=main1(n,a)
  print(ret1[0])
  print(len(ret1[1]))
  print(*ret1[1],sep='\n')

__starting_point()
