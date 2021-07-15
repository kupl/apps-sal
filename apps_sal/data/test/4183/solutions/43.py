import math
        
N = int(input())
T = []
for i in range(N):
    T.append(int(input()))
ans = T[0]

for i in range(1, N):
    ans = ans * T[i] // math.gcd(ans, T[i])

print(ans)
    


