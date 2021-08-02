n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
ans = [a[0]]
pref = [a[0]]
for q in range(1, m):
    ans.append(ans[-1] + a[q])
    pref.append(a[q])
for q in range(m, n):
    pref[q % m] += a[q]
    ans.append(ans[-1] + pref[q % m])
print(*ans)
