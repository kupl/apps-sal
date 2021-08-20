(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
bc = sorted([list(map(int, input().split())) for i in range(m)], key=lambda x: x[1])
bc.reverse()
flg = 0
cnt = 0
for i in range(n):
    if bc[flg][1] > a[i] and flg < m:
        a[i] = bc[flg][1]
        cnt += 1
        if cnt == bc[flg][0]:
            flg += 1
            cnt = 0
            if flg == m:
                break
    else:
        break
print(sum(a))
