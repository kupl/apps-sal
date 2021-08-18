import math
MOD = 10**9 + 7
N = int(input())
ans = 1
prime = set()
prime.add(2)
numofdiv = [0] * (N + 2)
for h in range(2, N + 1):
    flag = 1
    for j in prime:
        if h % j == 0:
            flag = 0
            break
    if flag == 1:
        prime.add(h)

for i in range(2, N + 1):
    for p in prime:
        while(i % p == 0):
            numofdiv[p] += 1
            i //= p
for q in range(N + 2):
    ans *= numofdiv[q] + 1
    ans %= MOD
print(ans)
