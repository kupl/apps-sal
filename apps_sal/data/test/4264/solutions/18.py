def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n = int(input())
  ans = 0
  for i in range(1, n+1):
    if len(str(i)) % 2 == 1:
      ans += 1
  print(ans)
def __starting_point():
  main()
__starting_point()
