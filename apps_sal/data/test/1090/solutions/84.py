import sys
input=sys.stdin.readline

N,K=(int(x) for x in input().rstrip('\n').split())
L = list(input())
now = L[0]
same = 0
for x in L[1:]:
  if x == now:
    same += 1
  else:
    now = x
res = same + K*2
if res > N-1:
  res = N-1
print(res)
