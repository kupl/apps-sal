n = int(input())
L = list(map(int,input().split()))
mini = L[0]
ans = 0

for l in L:
  if mini >= l:
    ans += 1
    mini = l
print(ans)
