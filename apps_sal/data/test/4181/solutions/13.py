N = int(input())
As = input().split(' ')
As = [int(As[i]) for i in range(N+1)]
Bs = input().split(' ')
Bs = [int(Bs[i]) for i in range(N)]
WIN = 0
for i in range(N):
  if Bs[i] > As[i]:
    WIN += As[i]
    Bs[i] -= As[i]
    As[i] = 0
    if Bs[i] > As[i+1]:
      WIN += As[i+1]
      Bs[i] -= As[i+1]
      As[i+1] = 0
    elif Bs[i] == As[i+1]:
      WIN += As[i+1]
      Bs[i] = 0
      As[i+1] = 0
    else:
      WIN += Bs[i]
      As[i+1] -= Bs[i]
      Bs[i] = 0
  elif Bs[i] == As[i]:
    WIN += As[i]
    Bs[i] = 0
    As[i] = 0
  else:
    WIN += Bs[i]
    As[i] -= Bs[i]
    Bs[i] = 0
print(WIN)
