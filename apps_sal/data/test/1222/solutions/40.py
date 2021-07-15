from collections import deque

def main():
  N=int(input())
  for n in range(N):
    x=ans.popleft()
    if x%10!=0:
      ans.append(10*x+(x%10)-1) # x equal y-1
    ans.append(10*x+(x%10)) # x equal y
    if x%10!=9:
      ans.append(10*x+(x%10)+1) # x equal y+1
  print(x)
  
def __starting_point():
  ans=deque([1,2,3,4,5,6,7,8,9])
  main()

__starting_point()
