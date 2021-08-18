
n, k = list(map(int, input().split()))

nn = []
ans = ''
for i in range(n):
    mid = input()
    if mid in nn:
        ans = mid
        continue
    nn.append(mid)
    n = len(nn)
if len(nn) == 1:
    ans = nn[0]
    ans = list(ans)
    ans[0], ans[1] = ans[1], ans[0]
    print(''.join(ans))
else:
    diff = []
    check = True
    cnt = {chr(97 + i): 0 for i in range(26)}
    for v in range(k):
        cnt[nn[0][v]] += 1
    for i in range(n):
        cnt2 = {chr(97 + i): 0 for i in range(26)}
        for j in range(k):
            cnt2[nn[i][j]] += 1
        if cnt != cnt2:
            print('-1')
            check = False
            break
    if check:
        check = False
        for i in range(n):
            check = False
            for j in range(i, n):
                diff = [l for l in range(k) if nn[i][l] != nn[j][l]]
                if len(diff) > 4:
                    check = True
                    print('-1')
                    break

            if check:
                break
        diff = [l for l in range(k) if nn[0][l] != nn[1][l]]
        mid = []
        check2 = False
        for i in range(k):
            if nn[0][i] in mid:
                check2 = True
                break
            mid.append(nn[0][i])
        if not check:
            res = list(nn[0])
            check = False
            for i in range(len(diff)):
                if check:
                    break
                for j in range(k):
                    if i == j:
                        continue
                    res[diff[i]], res[j] = res[j], res[diff[i]]
                    ans = ''.join(res)
                    check = True
                    for x in range(n):
                        mid = [ans[y] for y in range(k) if nn[x][y] != ans[y]]
                        if len(mid) == 2:
                            continue
                        elif len(mid) == 0 and check2:
                            continue
                        else:
                            check = False
                    if check:
                        print(ans)
                        check = True
                        break
                    res[diff[i]], res[j] = res[j], res[diff[i]]
            if not check:
                print('-1')
