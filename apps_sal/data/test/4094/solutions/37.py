K = int(input())
mod = 7
cnt = 0
for i in range(K):
    if mod % K == 0:
        cnt += 1
        break
    else:
        cnt += 1
        mod = (mod * 10 + 7) % K
if mod % K == 0:
    print(cnt)
else:
    print(-1)
