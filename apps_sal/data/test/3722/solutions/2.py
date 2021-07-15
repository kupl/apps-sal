N = int(input())
aa = input()
ab = input()
ba = input()
bb = input()
MOD = 10**9+7

if N <= 3:
    print(1)
    return

if (aa == ab == 'A') or (ab == bb == 'B'):
    print(1)
    return

if (aa+ab+ba == 'BAB') or (ab+ba+bb == 'BAA'):
    print(pow(2,N-3,MOD))
    return

pp = p = n = 1
for i in range(N-3):
    pp = p
    p = n
    n = (pp + p) % MOD
print(n)
