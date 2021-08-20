(n, p) = map(int, input().split())
(L, R) = ([], [])
for i in range(n):
    (l, r) = map(int, input().split())
    L.append(l)
    R.append(r)
ans = 0
for i in range(n):
    (l1, r1, l2, r2) = (L[i], R[i], L[(i + 1) % n], R[(i + 1) % n])
    (l_1, r_1, l_2, r_2) = (L[i], R[i], L[(i + 1) % n], R[(i + 1) % n])
    if l1 % p > 0:
        l1 += p - l1 % p
    if l2 % p > 0:
        l2 += p - l2 % p
    r1 -= r1 % p
    r2 -= r2 % p
    ans += 2000 * (r2 // p - l2 // p + 1) / (r_2 - l_2 + 1) + 2000 * (r1 // p - l1 // p + 1) / (r_1 - l_1 + 1) - 2000 * (r2 // p - l2 // p + 1) / (r_2 - l_2 + 1) * (r1 // p - l1 // p + 1) / (r_1 - l_1 + 1)
print(ans)
