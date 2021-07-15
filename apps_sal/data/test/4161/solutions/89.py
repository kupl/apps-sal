import math
K =  int(input())
ans = []
bc = [math.gcd(b, c) for b in range(1, K+1) for c in range(1, K+1)]
for a in range(1, K+1):
    for i in bc:
        x = math.gcd(a, i)
        ans.append(x)
print(sum(ans))
