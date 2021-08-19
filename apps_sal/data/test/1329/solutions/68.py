"""
75数の条件
約数の個数は各素因数の個数a1,a2,a3,...について
(a1+1)(a2+1)...(an+1)
75=3*5*5
->素因数の個数が2個, 4個, 4個になるような組み合わせ
(2,4,4)
(14,4)
(2,24)
(74)

求め方
1〜Nについて、素因数の数をdictに収めていく
->そのうち、4個以上あるものの組み合わせと2個以上あるものの組み合わせでカウントする
"""
import copy
N = int(input())
sosu = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
soinsu = dict()
for n in range(2, N + 1):
    if n in sosu:
        soinsu[n] = 1
    else:
        x = copy.deepcopy(n)
        i = 0
        while i < len(sosu):
            if x % sosu[i] == 0:
                soinsu[sosu[i]] += 1
                x = x // sosu[i]
            else:
                i += 1
ans = 0
cnt = [0, 0, 0, 0, 0]
tit = [2, 4, 14, 24, 74]
for (_, v) in soinsu.items():
    for i in range(5):
        cnt[i] += 1 if v >= tit[i] else 0
ans += cnt[1] * (cnt[1] - 1) // 2 * (cnt[0] - 2)
ans += cnt[2] * (cnt[1] - 1)
ans += cnt[3] * (cnt[0] - 1)
ans += cnt[4]
print(ans)
