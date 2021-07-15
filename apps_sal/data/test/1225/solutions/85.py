h = int(input())
count = 1

while(h > 1):
  count += 1
  h = int(h/2)

print(2**count - 1)
