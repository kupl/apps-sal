N = int(input())
L = list(map(int, input().split()))

L.sort()

ans = 0
for x in L[::2]:
  ans += x

print(ans)
