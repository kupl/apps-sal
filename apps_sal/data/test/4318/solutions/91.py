n = int(input())
h = list(map(int,input().split()))
num = 0
ans = 0
for i in h:
  if num <= i:
    ans += 1
    num = i
print(ans)
