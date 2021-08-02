import fractions

N = int(input())
A = list(map(int, input().split()))
D = [i for i in range(10**6 + 1)]
a_gcd = 0
for a in A:
    a_gcd = fractions.gcd(a, a_gcd)
if a_gcd > 1:
    print('not coprime')
    return

for i in range(2, 10**3 + 1):
    if D[i] == i:
        for n in range(i, 10**6 + 1, i):
            if D[n] == n:
                D[n] = i

p_set = set()
for a in A:
    d_set = set()
    while a > 1:
        if not D[a] in d_set:
            if D[a] in p_set:
                print('setwise coprime')
                return
            p_set.add(D[a])
            d_set.add(D[a])
        a //= D[a]
print('pairwise coprime')
