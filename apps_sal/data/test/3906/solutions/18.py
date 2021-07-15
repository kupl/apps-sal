from sys import stdin

height, width = list(map(int, stdin.readline().rstrip().split()))

def fib(n):
  if n < 2:
    return n
  a, b = [0, 1]
  for i in range(0, n):
    a, b = [b, a + b]
  return a

def solve(height, width):
  x = fib(width + 1) * 2
  return (x - 2 + fib(height + 1) * 2) % (pow(10, 9) + 7)

print(solve(height, width))

