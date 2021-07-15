n, k = map(int, input().split())
now = n
while True:
    if k == 2 ** (now - 1):
        print(now)
        break
    else:
        now -= 1
        k %= 2 ** now
