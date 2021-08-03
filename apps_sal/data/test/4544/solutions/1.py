n = int(input())
a = list(map(int, input().split()))

ans = 0

cnt = [0] * 100001

for i in a:
    cnt[i] += 1

for i in range(len(cnt) - 2):
    ans = max(ans, cnt[i] + cnt[i + 1] + cnt[i + 2])

print(ans)
