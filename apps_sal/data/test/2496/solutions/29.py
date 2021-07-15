from math import gcd

N = int(input())
A = list(map(int, input().split()))

prime = list(range(max(A) + 1))

for i in range(2, len(prime)):
    if prime[i] != i:
        continue
    for j in range(i, len(prime), i):
        if prime[j] != j:
            continue
        prime[j] = i

used = set()
pc = True
for a in A:
    used_this = set()
    while a != 1:
        div = prime[a]
        if div in used:
            pc = False
            break
        used_this.add(div)
        a //= div
    used.update(used_this)

if pc:
    print('pairwise coprime')
    return

buf = A[0]
for a in A[1:]:
    buf = gcd(buf, a)
if buf == 1:
    print('setwise coprime')
else:
    print('not coprime')
