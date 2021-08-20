(n, k) = map(int, input().split())
s = 0
cnt = 0
for i in range(1, n + 1):
    if s + 5 * i <= 240 - k:
        s += 5 * i
        cnt += 1
print(cnt)
