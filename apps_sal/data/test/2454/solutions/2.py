n = int(input())
cnt = [[] for _ in range(n)]
for i in range (n - 1):
    fr, to = list(map(int, input().split()))
    cnt[fr - 1].append(to - 1);
    cnt[to - 1].append(fr - 1);
l = 0
for i in range(n):
    if (len(cnt[i]) == 1):
        l += 1
ans = (n - l) * pow(2, n - l, 10 ** 9 + 7)
ans += l * pow(2, n - l + 1, 10 ** 9 + 7)
print(ans % (10 ** 9 + 7))

