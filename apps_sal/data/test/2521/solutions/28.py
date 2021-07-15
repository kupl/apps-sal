import heapq
def solve():
  n = int(input())
  a = list(int(i) for i in input().split())
  an = []
  a2n = a[n:2*n]
  a3n = []
  for i in range(n):
    heapq.heappush(an,a[i])
    heapq.heappush(a3n,-1*a[i+2*n])
  ta2n = a2n
  
  tmpsuman = sum(an)
  tmpsuma3n = -1*sum(a3n)
  
  suman = [tmpsuman]
  suma3n = [tmpsuma3n]
  
  for i in range(n):
    tmp = ta2n[i]
    tmpsuman += tmp
    heapq.heappush(an,tmp)
    tmpsuman -= heapq.heappop(an)
    
    suman.append(tmpsuman)
  for i in range(n):
    tmp = ta2n[n-i-1]
    tmpsuma3n += tmp
    heapq.heappush(a3n,-1*tmp)
    tmpsuma3n -= -1*heapq.heappop(a3n)
    suma3n.append(tmpsuma3n)

  ans = -10000000000000000
  for i in range(n+1):
    tmpans = suman[i]-suma3n[n-i]
    ans = max(ans,tmpans)
  print(ans)
solve()
