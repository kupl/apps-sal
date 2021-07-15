n = int(input())
a = [int(i) for i in input().split()]
pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] ^ a[i]
res = a[0]
for i in range(n):
    for j in range(i, n):
        res = max(res, pref[j + 1] ^ pref[i])
print(res)
