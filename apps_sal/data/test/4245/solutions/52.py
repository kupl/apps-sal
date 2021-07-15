A, B=map(int, input().split(" "))

outlet=1
tap=0

while outlet<B:
  outlet=outlet-1+A
  tap=tap+1
  if outlet>=B:
    break

print(tap)
