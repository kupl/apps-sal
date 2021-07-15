n, k = map(int, input().split())
rooms = input()
count = [0] * (n + 1)
for i in range(n):
    count[i] = count[i - 1]
    if rooms[i] == '0':
        count[i] += 1

ans = float('inf')
for i in range(n):
    if rooms[i] != '0':
        continue
    l = 0
    r = max(n - 1 - i, i)
    while l + 1 < r:
        m = (r + l) // 2
        if count[min(i + m, n - 1)] - count[max(-1, i - m - 1)] > k:
            r = m
        else:
            l = m
    ans = min(r, ans)
print(ans)
