(n, L, a) = list(map(int, input().split()))
ed = 0
ct = 0
for j in range(0, n):
    (t, l) = list(map(int, input().split()))
    ct = ct + (t - ed) // a
    ed = t + l
t = L
ct = ct + (t - ed) // a
print(ct)
