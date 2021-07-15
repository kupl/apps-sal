n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    if 5 - i >= k:
        cnt += 1
print(cnt // 3)
