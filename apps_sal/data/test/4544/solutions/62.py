n = int(input())
cnt = [0] * 100002

a = list(map(int, input().split()))

for v in a:
    cnt[v - 1] += 1
    cnt[v] += 1
    cnt[v + 1] += 1

print((max(cnt)))
