n = int(input())
al = list((int(input()) for _ in range(n)))
num = [0] * n
i = 0
cnt = 0
while True:
    if al[i] == 2:
        print(cnt + 1)
        break
    elif num[al[i] - 1] == 1:
        print(-1)
        break
    else:
        num[al[i] - 1] += 1
        i = al[i] - 1
        cnt += 1
