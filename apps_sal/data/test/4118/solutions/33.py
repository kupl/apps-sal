def multiply(a,b):
  return a * b if a < 10 and b < 10 else -1

print(multiply(*map(int, input().split())))
