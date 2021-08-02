q = int(input())

n = 10**6
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(n**0.5) + 1):
    if not is_prime[i]:
        continue
    for j in range(i * 2, n + 1, i):
        is_prime[j] = False

P = [0] * (10**6)

for i in range(1, 10**6 - 1):
    if is_prime[i + 1] == True and is_prime[(i + 2) // 2] == True:
        P[i + 1] = P[i] + 1
    else:
        P[i + 1] = P[i]

for i in range(1, q + 1):
    l, r = map(int, input().split())
    print(P[r] - P[l - 1])
