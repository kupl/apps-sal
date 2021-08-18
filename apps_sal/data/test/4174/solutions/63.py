n, x = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
for i in range(n + 1):
    if sum(l[:i]) <= x:
        cnt += 1
print(cnt)
