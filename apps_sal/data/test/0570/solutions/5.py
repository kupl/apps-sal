a, b = list(map(int, input().split()))
cnt = 0
while True:
    cnt += 1
    a -= cnt
    if a < 0:
        print('Vladik')
        break
    cnt += 1
    b -= cnt
    if b < 0:
        print('Valera')
        break

