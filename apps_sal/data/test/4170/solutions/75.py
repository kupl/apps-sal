N = int(input())
H = list(map(int, input().split()))
ans = 0
a = 0
for i in range(N - 1):
  if H[i] >= H[i+1]:
    a += 1
  else:
    ans = max(ans, a)
    a = 0
else:
  ans = max(ans, a)
print(ans)
