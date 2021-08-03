n, t = list(map(int, input().split()))
nearest_t = 200000
ans = 0
for i in range(n):
    s, d = list(map(int, input().split()))
    if s >= t and s < nearest_t:
        nearest_t = s
        ans = i + 1
    elif s < t:
        k = (t - s) // d
        if (t - s) % d:
            k += 1
        cur_t = s + d * k
        if cur_t < nearest_t:
            nearest_t = cur_t
            ans = i + 1
print(ans)
