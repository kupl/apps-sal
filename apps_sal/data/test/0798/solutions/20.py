a, b, c = [int(x) for x in input().split()]
for x in range(min(a+1, b+1)):
  if a-x <= c and c-a+x == b-x:
    print(x, b-x, a-x)
    return
print("Impossible")

