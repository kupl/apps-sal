import math
 
N = int(input())
 
M = int(math.sqrt(N))

ans = 0 
check = [True for _ in range(M + 1)]
e = [0 for _ in range(M + 1)]

for p in range(2, M + 1):
    if check[p] == True:
        for j in range(2, M // p + 1):
            check[p * j] = False

        while N % p == 0:
            N = N // p
            e[p] += 1
        
        ans += int((math.sqrt(1 + 8 * e[p]) - 1)/2)

if N > 1:
    ans += 1

print(ans)
