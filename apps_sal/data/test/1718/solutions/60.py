n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt, ttl = 1, k
while ttl < n:
    ttl += k - 1
    cnt += 1
print(cnt)
