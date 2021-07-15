n = input()
num = len(n) // 2
ans = 0
for i in range(num):
  if n[i] != n[len(n)-1-i]:
    ans += 1
print(ans)

