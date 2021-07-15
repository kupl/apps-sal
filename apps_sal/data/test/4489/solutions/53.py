blue = []
red = []
ans = 0
n = int(input())
for i in range(n):
  blue.append(input())
m = int(input())
for j in range(m):
  red.append(input())
word = set(blue)
for k in word:
  c = blue.count(k) - red.count(k)
  ans = max(ans,c)
print(ans)
