n = int(input())
dic = {}
ans = 0

for _ in range(n):
  x = input()
  if x not in dic:
    ans += 1
    dic[x] = 1


print(ans)
