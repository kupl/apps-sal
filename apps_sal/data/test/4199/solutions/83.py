N, K = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0
for i in l:
    if i >= K:
        cnt = cnt + 1

print(cnt)
