n = int(input())
cnt = 0
for i in range(3, n + 1):
    cnt += i * (i - 1)
print(cnt)
