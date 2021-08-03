k = int(input())
cnt = 1
mod = 7

for i in range(k):
    if mod % k == 0:
        break
    cnt += 1
    mod = (mod * 10 + 7) % k

if mod % k == 0:
    print(cnt)
else:
    print(-1)
