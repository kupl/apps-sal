N,A,B,C=map(int,input().split())

if A+B+C==0:
  print("No")
elif A+B+C==1:
  ans_list=[]
  for _ in range(N):
    com=input()
    if com=="AB":
      if A==1:
        A-=1
        B+=1
        ans_list.append("B")
      elif B==1:
        A+=1
        B-=1
        ans_list.append("A")
      else:
        print("No")
        break
    elif com=="AC":
      if A==1:
        A-=1
        C+=1
        ans_list.append("C")
      elif C==1:
        A+=1
        C-=1
        ans_list.append("A")
      else:
        print("No")
        break
    elif com=="BC":
      if B==1:
        B-=1
        C+=1
        ans_list.append("C")
      elif C==1:
        B+=1
        C-=1
        ans_list.append("B")
      else:
        print("No")
        break
  else:
    print("Yes")
    for ans in ans_list:
      print(ans)
else:
  com_list=[]
  for i in range(N):
    com_list.append(input())
  
  for i in range(N):
    com=com_list[i]
    if com=="AB":
      if i==0 and A==0 and B==0:
        print("No")
        break
      elif i==0:
        print("Yes")
      
      if i<N-1 and A+B+C==2 and A==1 and B==1 and com!=com_list[i+1]:
        if com_list[i+1]=="AC":
          A+=1
          B-=1
          print("A")
        elif com_list[i+1]=="BC":
          A-=1
          B+=1
          print("B")
      else:
        if A>=B:
          A-=1
          B+=1
          print("B")
        else:
          A+=1
          B-=1
          print("A")
    elif com=="AC":
      if i==0 and A==0 and C==0:
        print("No")
        break
      elif i==0:
        print("Yes")
      
      if i<N-1 and A+B+C==2 and A==1 and C==1 and com!=com_list[i+1]:
        if com_list[i+1]=="AB":
          A+=1
          C-=1
          print("A")
        elif com_list[i+1]=="BC":
          A-=1
          C+=1
          print("C")
      else:
        if A>=C:
          A-=1
          C+=1
          print("C")
        else:
          A+=1
          C-=1
          print("A")
    elif com=="BC":
      if i==0 and B==0 and C==0:
        print("No")
        break
      elif i==0:
        print("Yes")
      
      if i<N-1 and A+B+C==2 and B==1 and C==1 and com!=com_list[i+1]:
        if com_list[i+1]=="AB":
          B+=1
          C-=1
          print("B")
        elif com_list[i+1]=="AC":
          B-=1
          C+=1
          print("C")
      else:
        if B>=C:
          B-=1
          C+=1
          print("C")
        else:
          B+=1
          C-=1
          print("B")
