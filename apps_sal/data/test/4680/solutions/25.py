queue=list(map(int,input().split()))
queue.sort()
if queue[0]==5 and queue[1]==5 and queue[2]==7:
  print("YES")
else:
  print("NO")

