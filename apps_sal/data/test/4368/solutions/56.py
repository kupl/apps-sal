n, k = map(int, input().split())
cnt = 0
while n // k != 0:
    n = n // k
    cnt += 1

print(cnt + 1)
