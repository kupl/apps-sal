n = int(input())

s = list(map(int, input().split()))
t = []
v = 0

for i in range(n):
  c = 1/s[i]
  t.append(c)
  
for j in range(n):
  v += t[j]
  
ans = 1/v

print(ans)
