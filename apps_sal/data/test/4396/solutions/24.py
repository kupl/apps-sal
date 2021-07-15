n=int(input())
xu=[list(input().split()) for _ in range(n)]

result = 0
for i in range(n):
  if xu[i][1] == 'JPY':
    result += int(xu[i][0])
  else:
    result += float(xu[i][0]) * 380000
print(result)
