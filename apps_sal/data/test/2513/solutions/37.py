N = int(input())
S = str(input())

animal = ["S", "W"]

start = [[0, 0], [0, 1], [1, 0], [1, 1]]#最初の2つを指定

for i, j in start:
  ans = [-1] * N
  ans[0] = i
  ans[1] = j
  p = 0
  for k in range(N - 1):
    #print(ans)
    if p == 0:
      if k == 0:
        if S[k] == "o":
          if ans[k] == 0:
            ans[-1] = ans[1]
          else:
            ans[-1] = 1 - ans[1]
        else:
          if ans[k] == 0:
            ans[-1] = 1 - ans[1]
          else:
            ans[-1] = ans[1]
      else:
        if S[k] == "o":
          if ans[k] == 0:
            now = ans[k - 1]
            if ans[k + 1] == 1 - now:
              p = 1
            else:
              ans[k + 1] = now
          else:
            now = 1 - ans[k - 1]
            if ans[k + 1] == 1 - now:
              p = 1
            else:
              ans[k + 1] = now            
        else:
          if ans[k] == 0:
            now = 1 - ans[k - 1]
            if ans[k + 1] == 1 - now:
              p = 1
            else:
              ans[k + 1] = now
          else:
            now = ans[k - 1]
            if ans[k + 1] == 1 - now:
              p = 1
            else:
              ans[k + 1] = now
  
  #N == 3の時に備えて
  if ans[-1] == 0:
    if S[-1] == "o":
      if ans[-2] != ans[0]:
        p = 1
    else:
      if ans[-2] == ans[0]:
        p = 1
  else:
    if S[-1] == "o":
      if ans[-2] == ans[0]:
        p = 1
    else:
      if ans[-2] != ans[0]:
        p = 1
  
  if p == 0:
    #print(ans)  
    for i in range(N):
      if ans[i] == 0:
        print("S", end = "")
      else:
        print("W", end = "")
    return
    
print(-1)
            
        
        
        
        
          
          
          
          
