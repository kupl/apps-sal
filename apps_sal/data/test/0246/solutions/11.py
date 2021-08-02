def I(): return list(map(int, input().split()))


n, s = I()
cnt = n - min(200 + s, n + 1) + 1
for i in range(s, min(200 + s, n + 1)):
    if i - sum(map(int, str(i))) >= s:
        cnt += 1
print(cnt)
