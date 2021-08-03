a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    if i // 10000 == i % 10 and (i // 1000) % 10 == (i % 100) // 10:
        cnt += 1
print(cnt)
