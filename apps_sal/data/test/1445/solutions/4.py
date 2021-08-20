n = int(input())
ip = list(map(int, input().split()))
for i in range(n // 2):
    if i % 2 == 0:
        (ip[i], ip[n - i - 1]) = (ip[n - i - 1], ip[i])
    else:
        continue
for i in ip:
    print(i, end=' ')
