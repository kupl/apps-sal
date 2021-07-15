import collections
N = int(input())
A = list(map(int, input().split()))

#i + Ai
plus = [0] * N
#i - Ai
minus = [0] * N

for i in range(N):
  plus[i] = i + 1 + A[i]
  minus[i] = i + 1 - A[i]
  
#print(plus, minus)  
plus = dict(collections.Counter(plus))
minus = dict(collections.Counter(minus))

#print(plus)
#print(minus)

ans = 0
for i in list(plus.keys()):
  #print(i)
  if i in minus:
    #print(i)
    ans += plus[i] * minus[i]
    #print(ans)

print(ans)

