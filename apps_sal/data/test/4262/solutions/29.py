N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


def kaijo(x):
    ans = 1
    for i in range(x):
        ans = ans * (i + 1)
    return ans


def junban(dic):
    order = 1
    used = []
    for i in range(N):
        minus = 1
        for j in used:
            if dic[i] > j:
                minus += 1
        order += (dic[i] - minus) * kaijo(N - i - 1)
        used.append(dic[i])
    return order


Porder = junban(P)
Qorder = junban(Q)
if Porder >= Qorder:
    print(Porder - Qorder)
else:
    print(Qorder - Porder)
