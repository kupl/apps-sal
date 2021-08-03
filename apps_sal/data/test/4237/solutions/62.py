import math

A, B, C, D = list(map(int, input().split()))

cd = (C * D) // math.gcd(C, D)

pac, qac = divmod(A, C)
pad, qad = divmod(A, D)
pacd, qacd = divmod(A, cd)

pbc, qbc = divmod(B, C)
pbd, qbd = divmod(B, D)
pbcd, qbcd = divmod(B, cd)

pac = pac - 1 if qac == 0 else pac
pad = pad - 1 if qad != 0 else pad
pacd = pacd - 1 if qacd != 0 else pacd

ans = (pbc + pbd - pbcd) - (pac + pad - pacd)
print((B - A - ans + 1))
