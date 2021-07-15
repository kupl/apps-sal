'__author__'=='deepak Singh Mehta(learning to code)) '


def __starting_point():
  n = int(input())
  arr = list(map(int,input().split()))
  #cnt = 0
  flag = False
  for i in range(len(arr)):
    if arr[i]+1 in arr and arr[i]+2 in arr:
      flag = True
      break
  if flag:
    print("YES")
  else:
    print("NO")

__starting_point()
