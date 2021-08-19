def editarr(x, y, arr):
    l = len(arr)
    if abs(x) >= abs(y):
        for i in range(l):
            (arr[i][0], arr[i][1]) = (arr[i][1], arr[i][0])
    if x < 0:
        for i in range(l):
            arr[i][0] *= -1
    if y < 0:
        for i in range(l):
            arr[i][1] *= -1


k = int(input())
(x, y) = map(int, input().split())
ans = []
tx = abs(x)
ty = abs(y)
if tx >= ty:
    (tx, ty) = (ty, tx)
if k % 2 == 0 and (tx + ty) % 2 != 0:
    print(-1)
else:
    if tx + ty < k:
        if (tx + ty) % 2 == 0:
            m = (ty - tx) // 2
            ans.append([k - m, m])
        else:
            td = k - (tx + ty)
            ans.append([tx, ty + td])
            ans.append([tx + (k - td // 2), ty + td // 2])
        ans.append([tx, ty])
    elif ty - (k - tx % k) < k and (ty - (k - tx % k)) % 2 != 0:
        if (2 * k - (tx + ty)) % 2 == 0:
            td = 2 * k - (tx + ty)
            ans.append([tx + td // 2, k - (tx + td // 2)])
            ans.append([tx, ty])
        else:
            ans.append([tx, k - tx])
            td = ty - (k - tx)
            ans.append([tx + (k - td // 2), ans[-1][1] + td // 2])
            ans.append([tx, ty])
    else:
        ans.append([0, 0])
        for i in range(tx // k):
            ans.append([ans[-1][0] + k, 0])
        if ans[-1][0] != tx:
            ans.append([tx, k - abs(tx - ans[-1][0])])
        td = ty - ans[-1][1]
        if td % k == 0:
            flag = True
        else:
            flag = False
        for i in range(td // k):
            if flag == False and (ty - ans[-1][1]) % 2 == 0 and (ty - ans[-1][1] <= 2 * k):
                break
            ans.append([tx, ans[-1][1] + k])
        if ans[-1][1] != ty:
            td = ty - ans[-1][1]
            ans.append([tx + (k - td // 2), ans[-1][1] + td // 2])
            ans.append([tx, ty])
        ans.pop(0)
    editarr(x, y, ans)
    print(len(ans))
    for (a, b) in ans:
        print(a, b)
