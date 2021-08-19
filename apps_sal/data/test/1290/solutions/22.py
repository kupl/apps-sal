(n, m) = map(int, input().split())
c = list(map(int, input().split()))
cnt = [0] * n
for x in c:
    cnt[x - 1] += 1
print(min(cnt))
