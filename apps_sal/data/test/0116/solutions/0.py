def read():
    return list(map(int, input().split()))


(l1, r1, l2, r2, k) = read()
R = min(r1, r2)
L = max(l1, l2)
ans = max(R - L + 1, 0)
if L <= k <= R:
    ans = max(ans - 1, 0)
print(ans)
