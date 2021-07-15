a, b = list(map(int, input().split()))

if b != 100:
  ans = 100 ** a * b
else:
  ans = 100 ** a * (b+1)

print(ans)
