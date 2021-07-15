def ria():
  return [int(i) for i in input().split()]
ar=ria()
ar=ria()
kek=(ar[1]-ar[0])

for i in range(1,len(ar)):
  if ar[i]-ar[i-1]!=(ar[1]-ar[0]):
    print(ar[len(ar)-1])
    return

print(ar[len(ar)-1]+kek)

