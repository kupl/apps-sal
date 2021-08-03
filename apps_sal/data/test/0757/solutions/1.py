n, m, k = map(int, input().split())
t = list(map(int, input().split()))
t.sort(reverse=True)

m -= k
i = 0
if m > 0:
    while i < n:
        m -= t[i] - 1
        i += 1
        if m <= 0:
            break

print(i if m <= 0 else -1)
