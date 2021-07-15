x=int(input())
a,b=map(int,input().split())
max_b=b//x*x
if max_b>=a:
  print("OK")
else:
  print("NG")
