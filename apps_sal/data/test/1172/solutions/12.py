MOD = 10 ** 9 + 7
s = input()
Anum = 0
ABnum = 0
ABCnum = 0
q = 0
for c in s:
    if c == 'A':
        Anum = (Anum + pow(3, q, MOD)) % MOD
    elif c == 'B':
        ABnum = (ABnum + Anum) % MOD
    elif c == 'C':
        ABCnum = (ABCnum + ABnum) % MOD
    else:
        (Anum, ABnum, ABCnum) = (3 * Anum + pow(3, q, MOD), 3 * ABnum + Anum, 3 * ABCnum + ABnum)
        (Anum, ABnum, ABCnum) = (Anum % MOD, ABnum % MOD, ABCnum % MOD)
        q += 1
print(ABCnum)
