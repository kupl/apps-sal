from math import sqrt
N = int(input())
ans = []
add = ans.append
for k in filter(lambda p: N % p == 0, range(1, int(sqrt(N))+1)):
    add(N*k*(k-1)//2//k+k)
    k = N//k
    add(N*k*(k-1)//2//k+k)

print(*sorted(set(ans)))
