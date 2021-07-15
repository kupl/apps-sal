w,h,ｎ = list(map(int, input().split()))
ans = [[0]*(w) for i in range(h)]
for i in range(n):
  x,y,a = list(map(int, input().split()))
  if a == 1:
    for i in range(x):
      for j in range(h):
        ans[j][i] = 1
  elif a == 2:
    for i in range(x,w):
      for j in range(h):
        ans[j][i] = 1
  elif a == 3:
    for i in range(w):
      for j in range(y):
        ans[j][i] = 1
  elif a == 4:
    for i in range(w):
      for j in range(y,h):
        ans[j][i] = 1

cnt = 0
for i in ans:
  cnt += sum(i)
print((h*w - cnt))

