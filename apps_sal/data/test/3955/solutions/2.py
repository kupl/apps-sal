n, k, x = list(map(int, input().split()))
a = list(map(int, input().split()))

pref = [0 for el in a]
suff = [0 for el in a]

pref[0] = a[0]
for i in range(1, len(a)):
    pref[i] = pref[i-1] | a[i]

suff[-1] = a[-1]
for i in range(len(a)-2, -1, -1):
    suff[i] = suff[i+1] | a[i]

if n == 1:
    print(a[0]*x**k)
    return

sol = max((a[0]*x**k) | suff[1], pref[-2] | (a[-1]*x**k))
for i in range(1, len(a)-1):
    sol = max(sol, pref[i-1] | (a[i]*x**k) | suff[i+1])

print(sol)

