t = int(input())
for _ in range(t):
    n, x, m = list(map(int, input().split()))
    ansl = x
    ansr = x
    for _ in range(m):
        l, r = list(map(int, input().split()))
        if ansr >= l:
            ansr = max(r, ansr)
        if ansl <= r:
            ansl = min(l, ansl)

    print(ansr-ansl+1)

