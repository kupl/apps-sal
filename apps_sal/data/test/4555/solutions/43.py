A, B, K = list(map(int, input().split()))

upstart = max(B - K + 1, 0)
uplim = min(upstart + K, B)
ans = set([a for a in range(A, min(A + K, B))] + [b for b in range(upstart, uplim + 1)])
ans = sorted(list(ans))
for a in ans:
    if a < A:
        continue
    print(a)

