n = int(input())
out = 0
for i in range(1, n):
  out += n // i
  if n % i == 0:
    out -= 1
print(out)
