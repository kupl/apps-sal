N = int(input())
*p, = map(int, input().split())

LL = [0] + [i for i in range(N+1)]
RR = [i+1 for i in range(N+1)] + [N+1]

E = [(v,i+1) for i,v in enumerate(p)]
E.sort()

ans = 0
for v,i in E:
  r0 = RR[i]; r1 = RR[r0]
  l0 = LL[i]; l1 = LL[l0]
  RR[l0] = r0; LL[r0] = l0
  
  ans += ((r1 - r0)*(i-l0)+(r0-i)*(l0 - l1))*v

print(ans)
