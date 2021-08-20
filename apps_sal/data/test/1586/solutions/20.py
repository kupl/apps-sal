N = int(input())
if N % 2 == 1:
    print(0)
else:
    cnt = 0
    for i in range(1, N):
        if N >= 2 * 5 ** i:
            cnt += N // (2 * 5 ** i)
        else:
            break
    print(cnt)
