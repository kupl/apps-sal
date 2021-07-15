n = int(input())
A = list(map(int, input().split()))
max = -1
ans = True
ind = 1
for a in A:
  if a > max + 1:
    ans = False
    break
  if a == max + 1:
    max = a
  ind += 1
print(-1 if ans else ind)
