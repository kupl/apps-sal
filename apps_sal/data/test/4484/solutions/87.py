def main():
  N, M = [int(n) for n in input().split(" ")]

  if abs(N - M) >= 2:
    print((0))
  elif abs(N - M) == 1:
    print(((factorial(N) * factorial(M)) % 1000000007))
  else:
    print(((factorial(N) * factorial(M) * 2) % 1000000007))

def factorial(n):
  ret = 1
  for i in range(1, n + 1):
    ret = (ret * i) % 1000000007
  return ret
    
main()

