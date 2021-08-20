N = int(input())
a = list(map(int, input().strip().split()))
cnt = 0
for n in range(N):
    while True:
        if a[n] % 2 == 0:
            a[n] //= 2
            cnt += 1
        else:
            break
print(cnt)
