

H, W, M = map(int, input().split())

Hmax_temp = [0] * (H + 1)
Wmax_temp = [0] * (W + 1)
Hmax = 0
Wmax = 0
Bomb = dict()
for i in range(M):
    H_M, W_M = map(int, input().split())
    Hmax_temp[H_M] += 1
    Wmax_temp[W_M] += 1
    Bomb[(H_M, W_M)] = 1

Hmax = max(Hmax_temp)
Wmax = max(Wmax_temp)

y_max = []
for i in range(H + 1):
    if Hmax == Hmax_temp[i]:
        y_max.append(i)

x_max = []
for j in range(W + 1):
    if Wmax == Wmax_temp[j]:
        x_max.append(j)

flag = False
for i in y_max:
    for j in x_max:
        if (i, j) not in Bomb:
            flag = True
            break
    if flag:
        break

if flag:
    ans = Wmax + Hmax
else:
    ans = Wmax + Hmax - 1
print(ans)
