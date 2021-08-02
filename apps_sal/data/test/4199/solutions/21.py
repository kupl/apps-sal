n, k = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
for i in li:
    if i >= k:
        cnt += 1

print(cnt)
