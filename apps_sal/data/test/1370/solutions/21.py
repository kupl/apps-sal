H, W, K = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())
hsummation = [[int(S[0][k])]for k in range(W)]
for k in range(W):
    for j in range(1, H):
        hsummation[k].append(hsummation[k][j - 1] + int(S[j][k]))
# print(hsummation)
ans = float('inf')
anskouho = 0
h = 2**(H - 1)
for j in range(2**(H - 1)):
    h -= 1
    binh = "0" * (H - len(str(bin(h))) + 1) + str(bin(h))[2:]
    hlist = []
    for k in range(H - 1):
        if binh[-k - 1] == '1':
            hlist.append(k)
    hlist.append(-1)
    # print(hlist)
    anskouho = len(hlist) - 1
    now = 0
    while now < W:
        counter = [0 for _ in range(len(hlist))]
        while now < W:
            for l in range(len(hlist)):
                if l == 0:
                    counter[l] += hsummation[now][int(hlist[l])]
                    continue
                else:
                    counter[l] += - hsummation[now][hlist[l - 1]] + hsummation[now][hlist[l]]
            if max(counter) > K:
                anskouho += 1
                break
            else:
                now += 1
        if anskouho > ans:
            break
    else:
        ans = min(ans, anskouho)

        # print(counter)
# print(anskouho)
print(ans)
