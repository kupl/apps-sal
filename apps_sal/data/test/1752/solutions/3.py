n = int(input())

seq = sorted(map(int, input().split()))
if n <= 3:
    print(' '.join(map(str, seq)))
else:
    ans = [0 for x in range(n)]
    i = 0
    while i <= n // 2:
        try:
            ans[i] = seq[i * 2]
            ans[-i - 1] = seq[i * 2 + 1]
        except IndexError:
            pass
        i += 1
    print(' '.join(map(str, ans)))
