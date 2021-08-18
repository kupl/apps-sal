n, m = map(int, input().split())
aa = list(map(int, input().split()))
aa.sort()
# n^3でできる(一応)
# i日でできるかどうか
# できるだけ均一に並べたほうが良い
# j個使ってできるか
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ans = 0
        cnt = 0
        for k in range(j):
            now = aa[n - j + k]
            ans += max(0, now - cnt // i)
            cnt += 1
        # mページを超えたとき
        if ans >= m:
            print(i)
            return
print(-1)
