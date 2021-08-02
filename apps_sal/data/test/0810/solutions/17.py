import sys
M = 1000000007
def alele(): return list(map(int, sys.stdin.readline().strip().split()))
def ilele(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


a, b, n = ilele()
Ans = 0
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % M
for i in range(n + 1):
    s = str(a * i + b * (n - i))
    Noa = 0
    Nob = 0
    for j in s:
        if int(j) == a:
            Noa += 1
        elif int(j) == b:
            Nob += 1
    if Noa + Nob == len(s):
        Ans = (Ans + pow(fact[n - i] * fact[i], M - 2, M)) % M
print((Ans * fact[n]) % M)
