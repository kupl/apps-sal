n = int(input())
a = list(map(int, input().split()))
c = 0
for x in a:
  while x % 2 == 0:
    c += 1
    x //= 2
print(c)
