def num():
    from sys import stdin
    h, n = list(map(int, input().split()))
    magic = [list(map(int, stdin.readline().split())) for _ in range(n)]
    INF = float('inf')
    ans = [INF]*(h+1)
    ans[-1] = 0

    for i in range(h, 0, -1):
        if ans[i] != INF:
            for j, k in magic:
                if i-j < 0:
                    num = ans[i]+k
                    if ans[0] > num:
                        ans[0] = num
                else:
                    num = ans[i]+k
                    if ans[i-j] > num:
                        ans[i-j] = num
    return ans[0]
print((num()))



