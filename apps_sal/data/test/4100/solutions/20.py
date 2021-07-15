n, k, q = map(int,input().split())
l = [k-q] * n
for i in range(q):
  l[int(input())-1] +=1
for i in range(n):
  if l[i] > 0: print("Yes")
  else: print("No")
