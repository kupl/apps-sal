(n, s) = map(int, input().split())
cnt = 0
for i in range(n, 0, -1):
    cnt += s // i
    s %= i
print(cnt)
