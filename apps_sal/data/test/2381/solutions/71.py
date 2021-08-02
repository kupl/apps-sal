MOD = 10 ** 9 + 7

n, k = list(map(int, input().split()))
alst = list(map(int, input().split()))

alst.sort()

if n == k:
    ans = 1
    for num in alst:
        ans *= num
        ans %= MOD
    print(ans)
    return

if k == 1:
    print((alst[-1] % MOD))
    return

if alst[0] >= 0:
    ans = 1
    alst.sort(reverse=True)
    for i in range(k):
        ans *= alst[i]
        ans %= MOD
    print(ans)
    return

if alst[-1] <= 0:
    ans = 1
    if k % 2 == 1:
        alst = alst[::-1]
    for i in range(k):
        ans *= alst[i]
        ans %= MOD
    print(ans)
    return

blst = []
for num in alst:
    try:
        blst.append([abs(num), abs(num) // num])
    except ZeroDivisionError:
        blst.append([abs(num), 0])
blst.sort(reverse=True, key=lambda x: x[0])
if blst[k - 1] == 0:
    print((0))
    return

minus = 0
last_minus = 0
last_plus = 0
ans_lst = []
for i in range(k):
    if blst[i][1] == -1:
        minus += 1
        last_minus = blst[i][0]
    elif blst[i][1] == 1:
        last_plus = blst[i][0]
    else:
        print((0))
        return
    ans_lst.append(blst[i][0])

next_minus = 0
next_plus = 0
flg_minus = False
flg_plus = False

for i in range(k, n):
    if blst[i][1] == -1 and (not flg_minus):
        next_minus = blst[i][0]
        flg_minus = True
    if blst[i][1] == 1 and (not flg_plus):
        next_plus = blst[i][0]
        flg_plus = True
    if (flg_plus and flg_minus) or blst[i][1] == 0:
        break

if minus % 2 == 0:
    ans = 1
    for num in ans_lst:
        ans *= num
        ans %= MOD
    print(ans)

else:
    minus_s = last_minus * next_minus
    plus_s = last_plus * next_plus
    ans = 1
    if minus == k:
        ans_lst.remove(last_minus)
        ans_lst.append(next_plus)
    elif minus_s == plus_s == 0:
        if next_minus == 0:
            ans_lst.remove(last_minus)
            ans_lst.append(next_plus)
        else:
            print((0))
            return

    elif minus_s > plus_s:
        ans_lst.remove(last_plus)
        ans_lst.append(next_minus)
    else:
        ans_lst.remove(last_minus)
        ans_lst.append(next_plus)
    for num in ans_lst:
        ans *= num
        ans %= MOD
    print(ans)
