(p, q, l, r) = map(int, input().split())
arr_z = [0] * (p * 2)
i = 0
for k in range(p):
    t = list(map(int, input().split()))
    (arr_z[i], arr_z[i + 1]) = ((t[0], -1), (t[1], 1))
    i += 2
arr_z.sort()
arr = [False] * 1001
for i in range(q):
    t = list(map(int, input().split()))
    t[1] = t[1] - t[0]
    f = t[0]
    for j in range(l, r + 1):
        t[0] = f + j
        if arr[j] != True:
            tl = -1
            tr = p * 2
            while tr > tl + 1:
                m = (tr + tl) // 2
                if t[0] < arr_z[m][0]:
                    tr = m
                elif t[0] > arr_z[m][0]:
                    tl = m
                elif arr_z[m][1] == 1:
                    tr = m
                else:
                    tl = m
            if tr < p * 2 and arr_z[tr][0] <= t[0] + t[1] or (tr != 0 and arr_z[tr - 1][1] == -1):
                arr[j] = True
ans = 0
for i in arr[l:r + 1]:
    if i == True:
        ans += 1
print(ans)
