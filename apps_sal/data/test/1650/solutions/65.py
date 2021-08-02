L = input()
MOD = 10**9 + 7

eq = 1
less = 0
for n in L:
    if n == '1':
        eq, less = eq * 2, eq + less * 3
    else:
        less = less * 3
    eq %= MOD
    less %= MOD

print(((eq + less) % MOD))
