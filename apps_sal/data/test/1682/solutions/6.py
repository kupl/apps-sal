from sys import stdin, stdout
(n, k) = map(int, stdin.readline().split())
pricesb = list(map(int, stdin.readline().split()))
pricesa = list(map(int, stdin.readline().split()))
cnt = []
for i in range(n):
    cnt.append((pricesb[i] - pricesa[i], i))
cnt.sort()
ans = 0
for i in range(n):
    if i < k or cnt[i][0] < 0:
        ans += pricesb[cnt[i][1]]
    else:
        ans += pricesa[cnt[i][1]]
stdout.write(str(ans))
