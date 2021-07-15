N = int(input())
List = list(map(int,input().split()))
counter = 0
for item in List:
  while True:
    if item % 2 == 0:
      counter += 1
      item /= 2
    else:
      break
print(counter)
