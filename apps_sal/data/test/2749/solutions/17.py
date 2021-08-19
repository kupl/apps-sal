(h, w) = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
ans = [[0] * w for i in range(h)]
i = 0
j = 0
k = 0
flg = True
while i < h:
    ans[i][j] = str(k + 1)
    a[k] -= 1
    if a[k] == 0:
        k += 1
    if flg:
        j += 1
        if j == w:
            j -= 1
            i += 1
            flg = False
    else:
        j -= 1
        if j == -1:
            j += 1
            i += 1
            flg = True
for i in range(h):
    print(' '.join(ans[i]))
