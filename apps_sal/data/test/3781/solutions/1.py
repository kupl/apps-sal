T = int(input())
while(T):
  T -= 1
  N = int(input())
  L = sorted(list(map(int,input().split())))
  if( N & 1 ):
    print("Second")
    continue
  for j in range (N // 2):
    if L[ 2 * j ] != L[ 2 * j + 1 ]:
      print("First")
      break
    if( j + 1 == N // 2 ):
      print("Second")
