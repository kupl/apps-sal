c = [list(map(int,input().split())) for _ in range(3)]

check = False
for i in range(101):
  for j in range(101):
    for k in range(101):
      o = c[0][0] - i
      p = c[1][1] - j
      q = c[2][2] - k
      
      if o < 0 or p < 0 or q < 0:
        continue
      
      ls = [[i+o,i+p,i+q],[j+o,j+p,j+q],[k+o,k+p,k+q]]
      if ls == c:
        check = True
        break
        
print("Yes" if check else "No")
