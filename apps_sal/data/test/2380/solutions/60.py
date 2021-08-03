n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = {}

for i in range(n):
    if a[i] in cnt:
        cnt[a[i]] += 1
    else:
        cnt[a[i]] = 1

for i in range(m):
    b, c = list(map(int, input().split()))

    if c in cnt:
        cnt[c] += b
    else:
        cnt[c] = b

cnts = sorted(cnt.items())
cnt = 0
tot = 0
last = (0, 0)

while cnt < n:
    last = cnts.pop()
    tot += last[0] * last[1]
    cnt += last[1]

tot -= (cnt - n) * last[0]
print(tot)
