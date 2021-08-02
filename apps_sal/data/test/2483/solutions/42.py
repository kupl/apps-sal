n, c = map(int, input().split())
imos = [0 for _ in range(10 ** 5 + 1)]
ans = 0
channel = [[] for _ in range(30)]
for _ in range(n):
    s, t, c = map(int, input().split())
    channel[c - 1].append([s, t])

for lst in channel:
    lst.sort()
    before = 0
    for s, t in lst:
        start = max(before, s - 1)
        imos[start] += 1
        end = min(t, 10 ** 5 + 1)
        imos[end] -= 1
        before = end
tmp = 0
for num in imos:
    tmp += num
    ans = max(ans, tmp)
print(ans)
