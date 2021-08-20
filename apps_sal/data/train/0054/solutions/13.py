T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    A = map(int, input().split())
    cnt = [0] * 40
    for i in A:
        pw = 0
        while i > 1:
            i //= 2
            pw += 1
        cnt[pw] += 1
    for i in range(12):
        cnt[i + 1] += cnt[i] // 2
    if cnt[11] > 0:
        print('YES')
    else:
        print('NO')
