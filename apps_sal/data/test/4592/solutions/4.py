x = int(input())
a = []
def cont(y):
    n = 0
    while True:
          if n - int(y ** (1/2)) + 1 == 0:
               a.append(y)
               break
                
          for j in range(2,int(y ** (1/2)) + 1):
                 if y % j == 0:
                    y = y // j
                    a.append(j)
                    n = 0
                    break
                 else:
                    n = n + 1

ans = 1
for k in range(2, x + 1):
    cont(k)
for h in range(2, x + 1):
    ans = ans * (a.count(h) + 1)

print(ans % 1000000007)
