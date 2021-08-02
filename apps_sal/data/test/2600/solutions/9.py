import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]
    ptn = n + m - 2
    cnt = 0
    ans = []
    for length in range(n + m + 10):
        tmp = []
        for i in range(length + 1):
            j = length - i
            if 0 <= i < n and 0 <= j < m:
                tmp.append(a[i][j])
        if tmp:
            ans.append(tmp)

    len_ans = len(ans)
    res = 0
    for i in range(len_ans // 2):
        cnt = [0, 0]
        for val in ans[i]:
            cnt[val] += 1
        for val in ans[- i - 1]:
            cnt[val] += 1
        res += min(cnt)
    print(res)
