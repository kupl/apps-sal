n = int(input())
a = [int(i) for i in input().split()]
pref = []
s = 0
for i in range(n):
    s += a[i]
    pref.append(s)
mins = 1000
for i in range(n):
    for j in range(i, n):
        s = abs((pref[j] - pref[i]) - (pref[i] + (pref[n-1] - pref[j])))
        if s < mins:
            mins = s
print(mins)
