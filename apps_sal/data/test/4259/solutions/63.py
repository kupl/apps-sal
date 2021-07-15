K = int(input())
A,B = map(int,input().split())
status = "NG"
for i in range(A,B+1):
  if i%K==0:
    status="OK"
    break
    
print(status)
