ans = 0
t = []
tmp = 10
for i in range(5):
    t.append(int(input()))
    if t[i] % 10 != 0 and t[i] % 10 < tmp:
        tmp = t[i] % 10
flg = 0
for i in range(5):
    if (t[i] % 10 != tmp or flg == 1) and t[i] % 10 == 0:
        ans += t[i]
    elif (t[i] % 10 != tmp or flg == 1) and t[i] % 10 != 0:
        ans += (t[i] // 10 + 1) * 10
    elif t[i] % 10 == tmp and flg == 0:
        ans += t[i]
        flg = 1
print(ans)
