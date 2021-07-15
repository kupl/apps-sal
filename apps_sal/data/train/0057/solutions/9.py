
T = int(input())

for i in range(T):
  n = int(input())
  #n,m = map(int, input().split())
  #a,b = map(int, input().split())
  a = [int(i) for i in input().split()]
  #a = list(input())
  
  if a[-1]>a[0]:
    print('YES')
  else:
    print('NO')



