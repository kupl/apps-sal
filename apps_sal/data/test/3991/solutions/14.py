n = int(input())
l = [int(i) for i in input().split()]
sm = 0
MOD = 10**9 + 7
add = 0
sub = 0
l.sort()
p = 3 * (10**5) + 9
pow2 = [0] * p
pow2[0] = 1
for i in range(1, p):
    pow2[i] = (pow2[i - 1] * 2) % MOD
for i in range(n):
    add += l[i] * (pow2[i])
    sub += l[i] * (pow2[n - i - 1])
print((add - sub + MOD) % MOD)
