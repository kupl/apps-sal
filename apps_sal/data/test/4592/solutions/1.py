# 高速素因数分解
# """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


n = int(input())

count = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        pass
    else:
        soinsuu_list = factorization(i)
        for soinsu, jisu in soinsuu_list:
            count[soinsu] += jisu
ans = 1
mod = 10**9 + 7
for i in count:
    ans *= (i + 1)
    ans = ans % mod
print(ans)
