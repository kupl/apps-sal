N = int(input())
Alist = list(map(int,input().split()))

temp = len(Alist)
ansnum = len(list(set(Alist)))

if ansnum == temp:
  print ("YES")
else :
  print ("NO")
