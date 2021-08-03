from bisect import bisect_left
N, M = list(map(int, input().split()))
s = input()
safe = []
cnt = 0
for i, m in enumerate(s):
    if m == '1':
        cnt += 1
        if cnt == M:
            print((-1))
            break
    else:
        safe += [i]
        cnt = 0
else:
    ps = N
    ans = []
    while ps != 0:
        ind = bisect_left(safe, ps - M)
        ans += [ps - safe[ind]]
        ps = safe[ind]
    print((*ans[::-1]))
