n = int(input())
a = [int(input()) for i in range(n)]
cnt = 0

if not a.count(2):
    print('-1')
else:
    i = 0
    while True:
        cnt += 1
        if a[i] == 2:
            print(cnt)
            break
        elif a[i] == i + 1 or cnt > n:
            print('-1')
            break
        i = a[i] - 1
