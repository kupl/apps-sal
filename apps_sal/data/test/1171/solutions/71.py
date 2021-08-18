n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0

for l in range(n):
    for r in range(n + 1)[::-1]:
        if l <= r and 0 <= (l + n - r) <= k:
            q = v[:l] + v[r:n]
            q.sort(reverse=True)

            for i in range(k - (l + n - r)):
                if q == []:
                    break
                if q[-1] < 0:
                    q.pop()
                else:
                    break

            ans = max(ans, sum(q))
        else:
            continue

print(ans)
