n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

DD = a[0]
DP = b[0]
PD = a[0]
PP = b[0]

for i in range(1, n):
    tDD = max(DP + a[i], PP + a[i])
    tPD = max(PD + b[i], DD + b[i])
    tDP = max(DP + b[i], PP + b[i])
    tPP = max(PD + c[i], DD + c[i])

    DD = tDD
    PD = tPD
    DP = tDP
    PP = tPP

if n == 1:
    sol = DD
else:
    sol = max(DD, PD)

print(sol)
