N = int(input())
cnt = 0
if N % 2 == 1:
    print(0)
else:
    for i in range(1, N):
        if N >= (2 * (5**i)):
            cnt += N // (2 * (5**i))
        else:
            break
    print(cnt)
