n,t=int(input()),0
AB=[list(map(int,input().split())) for _ in range(n)]
AB.sort(key=lambda X: X[1])

for ab in AB:
  t += ab[0]
  if t > ab[1]:
    print("No")
    return
    
print("Yes")
