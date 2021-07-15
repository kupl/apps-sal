N = int(input())
x = [0 for i in range(N)]
u = ['' for i in range(N)]
for i in range(N):
  x[i], u[i] = map(str, input().split())
  x[i] = float(x[i])

money = 0
for i in range(N):
  if u[i] == 'JPY':
    money += x[i]
  else:
    money += x[i] * 380000.0
print(money)
