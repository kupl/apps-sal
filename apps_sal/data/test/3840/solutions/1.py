n = int(input())
if n == 1 or n & 1 == 0:
    print(-1)
else:
    t = list(map(int, input().split()))
    (s, k) = (0, n // 2 - 1)
    for i in range(n - 1, 1, -2):
        p = max(t[i], t[i - 1])
        t[k] = max(0, t[k] - p)
        s += p
        k -= 1
    print(s + t[0])
