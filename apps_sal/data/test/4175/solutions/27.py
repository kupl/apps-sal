n=int(input())
w=[input() for i in range(n)]
if len(w) != len(set(w)):
  print("No")
  return
for i in range(n -1):
  if w[i][-1] != w[i+1][0]:
    print("No")
    return
print("Yes")
