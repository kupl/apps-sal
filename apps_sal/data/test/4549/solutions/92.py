H,W = map(int,input().split())

canvas = []

for i in range(H):
  canvas.append(list(input()))
  
#print(canvas)
for i in range(H):
  for j in range(W):
    cnt = 0
    if canvas[i][j] == "#":
      for h in range(-1,2):
        for w in range(-1,2):
          if canvas[min(max(i+h,0),H-1)][min(max(j+w,0),W-1)]=="#" and (abs(h)+abs(w))%2==1:
            cnt+=1
      if cnt==0:
        print("No")
        return
print("Yes")
