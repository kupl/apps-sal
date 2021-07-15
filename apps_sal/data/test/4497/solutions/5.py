s = int(input())
t = 1
for i in range(1,8,1):
  if(s >= (2 ** i)):t = 2 ** i
print(t)
