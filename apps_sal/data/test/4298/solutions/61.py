n,d = list(map(int,input().split(" ")))
d = d*2 + 1
answer = 0
while n >0:
  n-=d
  answer += 1
  
print(answer)

