n = int(input())
A = list(map(int, input().split()))
a = max(A)
acc = 0
ans = 1
for b in A:
  if b == a:
    acc += 1
  else:
    acc = 0
  ans = max(ans, acc)
print(ans)

