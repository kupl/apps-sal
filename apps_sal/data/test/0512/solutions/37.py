N = int(input())
AB = [0] * N
L = [[-1] * 2 for i in range(2 * N + 1)]
for i in range(N):
  a, b = list(map(int, input().split()))
  AB[i] = [a, b]
  if a != -1:
    if L[a] == [-1, -1]:
      L[a] = [1, i]
    else:
      print("No")
      return
  if b != -1:
    if L[b] == [-1, -1]:
      L[b] = [0, i]
    else:
      print("No")
      return   
    
  
#print(L)  
  
DP = [False] * (2 * N + 1)
DP[0] = True
for i in range(2, 2 * N + 1, 2):
  for j in range(1, i, 2):#j ~ iを一つとして考える
    if DP[j - 1]:#Falseならそもそも考えなくてOK
      x = int((i - j + 1) / 2)#(j, j+x), (j+1, j+1+x), ... , (i-x, i)
      T = True
      for k in range(j, i + 1):#(k, k + x) or (k - x, k)
        if L[k] == [-1, -1]:
          continue
        else:
          p, q = L[k]#p:向き, q:人のid
          if p == 0 and (k - x >= j):#k は大きい方の値 #k - xに相方が入れればOK
            if AB[q][0] == -1:#相方の位置未定
              if L[k - x] == [-1, -1]:
                continue
              else:
                T = False
            elif AB[q][0] == k - x:#相方がk-x
              continue
            else:#相方が違うところにいる
              T = False
          elif p == 1 and (k + x <= i):#k は小さい方の値 #k + xに相方が入れればOK
            if AB[q][1] == -1:
              if L[k + x] == [-1, -1]:
                continue
              else:
                T = False
            elif AB[q][1] == k + x:
              continue
            else:
              T = False 
          else:
            T = False
      if T:
        DP[i] = True
        
  #print(DP)        
if DP[-1]:
  print("Yes")
else:
  print("No")
  
    


