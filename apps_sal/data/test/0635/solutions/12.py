n, s = map(int, input().split(' '))

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

solution = False

if(a[0] == 1):
  if(a[s - 1] == 1):
    solution = True
  elif(b[s - 1] == 1):
    for i in range(s, n):
      if(a[i] == 1 and b[i] == 1):
        solution = True
        break

if solution:
  print("YES")
else:
  print("NO")
