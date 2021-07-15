def divisor(n):
  list1 = []
  for i in range(1, int(n ** (0.5)) + 1):
    if n % i == 0:
      list1.append(i)
      list1.append(int(n / i))
  list1 = list(set(list1))
  return len(list1) - 1

def function(n):
  ans = 0
  if n >= 2:
    ans += 1
  for i in range(2, int(n ** (0.5)) + 1):
    m = n
    if m % i == 0:
      while m % i == 0:
        m = int(m / i)
      if m % i == 1:
        ans += 1
  ans += divisor(n - 1)
  return ans
n = int(input())
print(function(n))
