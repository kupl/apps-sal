N = int(input())
H = list(map(int, input().split()))
ans = 0
maxH = 0
for i in H:
  if maxH <= i:
    ans += 1
    maxH = i
print(ans)

