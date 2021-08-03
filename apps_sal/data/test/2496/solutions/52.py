import math

N = int(input())
A = list(map(int, input().split()))

g = 0
for a in A:
    g = math.gcd(g, a)
if g != 1:
    print('not coprime')
    return

is_prime = [1] * 1000001
D = [0] * 1000001

for i in range(2, 1001):
    if is_prime[i]:
        D[i] = i
        j = 2 * i
        while j <= 1000000:
            if is_prime[j]:
                D[j] = i
                is_prime[j] = 0
            j += i
for i in range(1001, 1000001):
    if is_prime[i]:
        D[i] = i

count = [0] * 1000001
for a in A:
    k = a
    pre = 0
    while k != 1:
        if pre != D[k]:
            count[D[k]] += 1
            if count[D[k]] == 2:
                print('setwise coprime')
                return
        pre = D[k]
        k = int(k / D[k])
print('pairwise coprime')
