n=int(input())
h=list(map(int, input().split()))

def solve():
  h[0] -= 1
  for i in range(1, n):
    if h[i-1] > h[i]:
      return False
    if h[i-1] == h[i]:
      continue
    h[i] -= 1
  return True

print('Yes' if solve() else 'No')
