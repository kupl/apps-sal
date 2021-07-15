def main(n,a):
  # F:ゲームの先行
  # S:ゲームの後行
  if n%2==0:
    # ゲームの先行Fがnimの先行になる。
    # nimはF先行。Fはnimのxor和が0以上になるようにしたい。Sはぴったり0にしたい
    # Fは大きいものから順に同じ皿に置いていけばいい。逆にこれでも0になってしまう場合はSが勝つ。
    a.sort()
    num0,num1=0,0
    for i,x in enumerate(a):
      if i%2:
        num0+=x
      else:
        num1+=x
    return num0!=num1
  else:
    # ゲームの後行Sがnimの先行になる。
    # nimはS先行。Fはnimのxor和が0になるようにしたい。Sは0以上にしたい
    return False
    pass
t=int(input())
nary=[]
aary=[]
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  nary.append(n)
  aary.append(a)
for n,a in zip(nary,aary):
  print(('First' if main(n,a) else 'Second'))


