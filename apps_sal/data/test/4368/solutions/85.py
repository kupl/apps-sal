N, K = list(map(int, input().split()))
cnt = 0
while N > 0:
    cnt += 1
    N //= K
print(cnt)
