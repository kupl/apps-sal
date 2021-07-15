import numpy as np #numpyの練習がてら
n = int(input())
tmp = list(map(int,input().split()))

mod = 10**9 + 7
a = np.array(tmp,np.int64)

ans = 0
for i in range(60 + 1):
    b = (a >> i) & 1 #すべてのaについて2**n乗目のビットが1か否か
    iti = np.count_nonzero(b) #すべてのaのうち2**n乗目が1であるものの個数
    zero = n - iti #同様に0であるものの個数
    ans += (iti * zero) * pow(2,i,mod) % mod#片方1で片方0なら1なので1の個数×0の個数
ans %= mod
print(ans)

