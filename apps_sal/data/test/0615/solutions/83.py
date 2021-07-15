N = int(input())
A = [ int(x) for x in input().split()]

S = [0]

for a in A:
    S += [ S[-1] + a ]

l = 0
r = 2
ans = float('inf') 

for i in range(1, N-1):
    while S[i] - S[l+1] > S[l]:
        l += 1

    while S[N] - S[r+1] > S[r] - S[i]:
        r += 1

    a = S[l]
    b = S[i] - S[l]
    c = S[r] - S[i]
    d = S[N] - S[r]
  
    ans = min(ans, max(a,b,c,d) - min(a,b,c,d))
print(ans)

