n, a, b, c = map(int, input().split())
q = [input() for i in range(n)]
ab, ac, bc = "AB", "AC", "BC"
ans = []
for i in range(n):
  
  if((q[i] == ab and a == b == 0)
  or (q[i] == ac and a == c == 0) 
  or (q[i] == bc and b == c == 0)):
      print("No")
      return
      
  elif(q[i] == ab and [a, b, c] == [1, 1, 0] and i != n - 1):
    if q[i+1] == ac: 
      a, b = a+1, b-1
      ans.append("A")
    else:
      a, b = a-1, b+1
      ans.append("B")     
      
  elif(q[i] == ac and [a, b, c] == [1, 0, 1] and i != n - 1):
    if q[i+1] == ab:
      a, c = a+1, c-1
      ans.append("A")
    else:
      a, c = a-1, c+1
      ans.append("C")
      
  elif(q[i] == bc and [a, b, c] == [0, 1, 1] and i != n - 1):
    if q[i+1] == ab:
      b, c = b+1, c-1
      ans.append("B")
    else:
      b, c = b-1, c+1
      ans.append("C")
      
  elif q[i] == ab:
    if a > b:
      a, b = a-1, b+1
      ans.append("B")
    else:
      a, b = a+1, b-1
      ans.append("A")
      
  elif q[i] == ac:
    if a > c:
      a, c = a-1, c+1
      ans.append("C")
    else:
      a, c = a+1, c-1
      ans.append("A")
      
  elif q[i] == bc:
    if b > c:
      b, c = b-1, c+1
      ans.append("C")
    else:
      b, c = b+1, c-1
      ans.append("B")

print("Yes")
for i in range(n):
  print(ans[i])
