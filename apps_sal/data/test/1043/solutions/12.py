import sys
input = sys.stdin.readline
import heapq as hq
n = int(input())
a = list(map(int,input().split()))
frn = a.index(-1)+1
t = n.bit_length()
if frn == n:
  print(0)
  return
ans = a[n-1]
x = (frn-1).bit_length()
q = []
hq.heapify(q)
for i in range(1,t)[::-1]:
  for j in range(2**(i-1)-1,2**i-1):
    hq.heappush(q,a[j])
  y = hq.heappop(q)
  if y >= 0:
    ans += y
  else:
    break
print(ans)
