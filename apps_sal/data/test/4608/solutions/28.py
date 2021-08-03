N = int(input())
a = [int(input()) for _ in range(N)]
cnt = 0
on = 0
for _ in range(N):
    cnt += 1
    if a[on] == 2:
        print(cnt)
        return
    on = a[on] - 1
print(-1)
