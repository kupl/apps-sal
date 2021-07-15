a, b, c, x, y = map(int, input().split())

answer = 7000000000
for i in range(100001):
  amount = i*2*c + max(0, x-i)*a + max(0, y-i)*b
  if answer > amount:
    answer = amount
print(answer)
