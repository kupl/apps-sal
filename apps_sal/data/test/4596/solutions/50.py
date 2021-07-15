N = int(input())
A = list(map(int, input().split()))

def cnt(x):
  ret = 0
  while x%2 == 0:
    ret += 1
    x //= 2
  return ret

ans = 30
for a in A:
  ans = min(ans, cnt(a))

print(ans)
