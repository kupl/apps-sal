n, x, y = map(int, input().split())
ans = [0] * (n-1)
for i in range(1, n):
  for j in range(i+1, n+1):
    ans[min(abs(i-j), abs(x-i)+abs(j-y)+1, abs(y-i)+abs(j-x)+1)-1] += 1
for i in range(n-1):
  print(ans[i])
