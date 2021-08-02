n = int(input())
a = [int(input()) for i in range(n)]
cnt = 0

if 2 not in a:
    print(-1)
    return

x = 1
for i in range(n - 1):

    x = a[x - 1]
    cnt += 1

    if x == 2:
        print(cnt)
        return

print(-1)
