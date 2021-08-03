L = input()
n = len(L)
csum_1 = [0] * n
csum_0 = [0] * n
now1 = 0
now0 = 0
for i in range(n):
    if L[i] == '1':
        now1 += 1
    else:
        now0 += 1
    csum_1[i] = now1
    csum_0[i] = now0

mod = 10**9 + 7
ans = 0
# iは、「最初にL[i]=1かつai=0かつbi=0となるindex」
for i in range(n):
    if L[i] == '1':
        p = 1
        # 自分より左側の0の度に2パターン増加
        if i >= 1:
            p *= pow(2, csum_1[i - 1], mod)
        # print(p)
        # 自分より右側はどの桁も3パターン増加
        p *= pow(3, n - i - 1, mod)
        # print(p)
        ans += p
        ans %= mod
# L=a+bの場合
p = pow(2, csum_1[-1], mod)
# print(p)
ans = (ans + p) % mod
print(ans)
