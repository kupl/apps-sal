n = int(input())
k = int(input())
cnt = 1
for _ in range(n):
    if cnt <= k:
        cnt *= 2
    else:
        cnt += k
print(cnt)
