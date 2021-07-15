import sys
input = sys.stdin.readline

mm = 10**10
k = mm.bit_length()
K = 1<<k
nu = lambda L: int("".join([bin(K+a)[-k:] for a in L[::-1]]), 2)
st = lambda n: bin(n)[2:] + "0"
li = lambda s: [int(a, 2) if len(a) else 0 for a in [s[-(i+1)*k-1:-i*k-1] for i in range(200001)]]

n,m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [0]*100001

for i in a:
    b[i] += 1
    
c = li(st(nu(b)*nu(b)))
ans = 0
for i in range(200001)[::-1]:
    if c[i] > 0:
      p = min(m,c[i])
      m -= p
      ans += i*p
      if m == 0:
        break
print(ans)
