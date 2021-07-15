a,b,c = map(int, input().split())
for i in range(1,b):
  if (a*i+c)%b == 0:
    print("YES")
    break
else:
  print("NO")
