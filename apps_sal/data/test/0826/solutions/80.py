n = int(input())
ans = n
cnt = 0
while cnt <= n:
    cnt += 100000
    if cnt * (cnt + 1) // 2 > n + 1:
        cnt -= 100000
        break
while cnt <= n:
    cnt += 1
    if cnt * (cnt + 1) // 2 > n + 1:
        cnt -= 1
        break
print(ans - cnt + 1)
