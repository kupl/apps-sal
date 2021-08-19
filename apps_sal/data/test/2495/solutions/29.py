n = int(input())
a = list(map(int, input().split()))
cnt = [0, 0]
for (i, x) in zip([0, 1], [1, -1]):
    now = 0
    for aj in a:
        now += aj
        if now == 0:
            cnt[i] += 1
            now = x
        elif now * x < 0:
            cnt[i] += abs(now - x)
            now = x
        x *= -1
print(min(cnt))
