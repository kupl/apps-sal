n, k = list(map(int, input().split()))


def ab(v):
    if 2 <= v <= n + 1:
        return v - 1
    elif n + 2 <= v <= 2 * n:
        return 2 * n + 1 - v
    else:
        return 0


ans = 0
for i in range(2, 2 * n + 1):
    ans += ab(i) * ab(i - k)

print(ans)
