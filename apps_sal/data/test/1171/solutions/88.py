(N, K) = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for anum in range(min(N, K) + 1):
    owned = V[:anum]
    for bnum in range(min(N, K) - anum + 1):
        if bnum > 0:
            owned.append(V[-bnum])
        owned.sort()
        cdnum = K - (anum + bnum)
        total = 0
        for v in owned:
            if v < 0 and 0 < cdnum:
                cdnum -= 1
            else:
                total += v
        ans = max(ans, total)
print(ans)
