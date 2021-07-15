n,k = list(map(int, input().split()))

s = {i:0 for i in range(n+1)} 

for i in range(k):
  d = int(input())
  a = list(map(int, input().split()))
  for i in a:
    s[i] += 1

cnt = -1

for i in s:
  if s[i] == 0:
    cnt +=1

print(cnt)


