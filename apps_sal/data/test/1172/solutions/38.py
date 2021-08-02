S = input()
MOD = 10**9 + 7

A = 0
AB = 0
ABC = 0
prd = 1

for s in S:
    if s == 'A':
        A += prd
    elif s == 'B':
        AB += A
    elif s == 'C':
        ABC += AB
    else:
        a = A * 3 + prd
        ab = AB * 3 + A
        abc = ABC * 3 + AB
        A, AB, ABC = a, ab, abc
        prd *= 3
    A %= MOD
    AB %= MOD
    ABC %= MOD
    prd %= MOD

print(ABC)
