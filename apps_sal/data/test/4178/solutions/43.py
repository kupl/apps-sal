N = int(input())
List = list(map(int,input().split()))
flag = 0
for i in range(1,N):
  if List[-(i+1)] <= List[-i]:
    continue
  elif List[-(i+1)] ==List[-i]+1:
    List[-(i+1)] -= 1
  else:
    print('No')
    return
print('Yes')
