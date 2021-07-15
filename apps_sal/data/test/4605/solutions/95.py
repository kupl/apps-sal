def FindSumOfDigits(n):
  Sum = 0
  while n>0:
    Sum += n%10
    n //= 10
  return Sum

N, A, B = list(map(int, input().split()))
total = 0
for i in range(N):
  Sum = FindSumOfDigits(i+1)
  if A <= Sum and Sum <= B:
    total += i+1

print(total)

