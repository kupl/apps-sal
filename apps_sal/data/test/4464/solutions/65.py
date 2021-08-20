(a, b, c) = map(int, input().split())
cnt = 0
for i in range(1, 10 ** 5):
    if a * i % b == c:
        print('YES')
        break
    else:
        cnt += 1
        if cnt == 10 ** 5 - 1:
            print('NO')
            break
