n = int(input())
btn = [0]
for i in range(n):
  btn.append(int(input()))
see = [0 for i in range(n+1)]
  
now = 1
cnt = 0

see[now] = 1
while True:
  now = btn[now]
  cnt += 1
  
  if now == 2:
    print(cnt)
    break
  
  if see[now] == 1:
    print((-1))
    break
  
  see[now] = 1

