
import sys
input = sys.stdin.readline
# 文字列をinput()した場合、末尾に改行が入るので注意
def main():
  n,m=list(map(int,input().split()))
  a=sorted(list(map(int,input().split())))
  import bisect
  # 解説の二分探索
  # あるXを定め、X以上になる握手の組み合わせが何通りあるか計算。M個以上になる最大のXを探す
  # [l,r)半開区間
  l,r=0,a[-1]*2+1
  while r-l>1:
    x=(l+r)//2
    cnt=0
    for ai in a:
      cnt+=n-bisect.bisect_left(a,x-ai)
    # x以上がm個以上ある->x~r-1に求めるものがある
    if cnt>=m:
      l=x
    else:# x以上がm個未満ある->l~x-1に求めるものがある
      r=x
  x=(l+r)//2
  ans=0
  cnt=0
  a_=0
  cs_a=[0]
  for ai in a:
    a_+=ai
    cs_a.append(a_)
  for ai in a:
    bi=bisect.bisect_right(a,x-ai)
    cnt+=n-bi
    ans+=cs_a[-1]-cs_a[bi]+(n-bi)*ai
  print((ans+(m-cnt)*x))

def __starting_point():
  #import datetime
  #print(datetime.datetime.now())
  main()
  #print(datetime.datetime.now())

__starting_point()
