X = int(input())
ans = 0
Y = 100
while Y < X:
  Y += Y // 100
  ans += 1
print(ans)

