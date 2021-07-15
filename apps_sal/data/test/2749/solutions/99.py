h, w = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
color = [[0]*w for i in range(h)]
loch = 0
locw = 0
for i in range(n):
  for j in range(a[i]):
    color[loch][locw]=str(i+1)
    if loch % 2 == 0:
      if locw != w-1:
        locw+=1
      else:
        loch+=1
    else: 
      if locw != 0:
        locw-=1
      else:
        loch+=1

for i in range(h):
  print((" ".join(color[i])))

