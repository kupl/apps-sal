n = int(input())
cnt = 0
for i in range(1, n):
    u, v = map(int, input().split())
    l = min(u, v)
    h = max(u, v)
    cnt -= l * (n - h + 1)
    cnt += i * (n - i + 1)
cnt += n

print(cnt)
