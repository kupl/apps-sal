(n, k, M) = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
S = sum((t[j] for j in range(k)))
ans = 0
for i in range(n + 1):
    if i * S > M:
        break
    else:
        p = (k + 1) * i
        R = M - i * S
        for j in range(k):
            if R < t[j]:
                break
            else:
                q = min(n - i, R // t[j])
                R -= q * t[j]
                p += q
        ans = max(ans, p)
print(ans)
