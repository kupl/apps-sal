#n = int(input()) #入力
#a, b = (int(x) for x in input().split())
#a, b = map(int, input().split())

#a = [int(x) for x in input().split()]
#a = list(map(int, input().split()))
#a = [list(map(int,input().split(" "))) for i in range(N)]   #2次元


#a.sort() # C++ の sort(a.begin(), a.end());
#a.append(3) # C++ の a.push_back(3);


#return # return 0 的な。終了できる。
## 整数の切り捨て除算は // (ダブルスラッシュ)


#a[始まりの位置: 終わりの位置: スライスの増分] # (a は配列)


#import numpy as np  #importに100 ms 程度かかる。
import math
import copy
import string
#math.gcd(a, b) で、gcd 計算できる。
#math.pi は円周率。

INF = int(10**18) #べき乗 C++ の pow(10, 18) or 1e18;
pi = math.pi

MOD = 1000000007
#MOD = 1000000009
#MOD = 998244353




#繰り返し2乗法
#N^aの、Mで割った余りを求める。
def my_pow(N, a, M):
    if(a == 0):
        return 1
    else:
        if(a % 2 == 0):
            tempo = my_pow(N, a/2, M)
            return (tempo * tempo) % M
        else:
            tempo = my_pow(N, a - 1, M)
            return (tempo * N) % M




#N_C_a を M で割った余り
def my_combination(N, a, M):
    res = 1

    for i in range(0, a):
        res *= N - i
        res %= M

    for i in range(0, a):
        res *= my_pow(i + 1, M - 2, M)
        res %= M

    return res




#N_C_i を M で割った余りを、v[i] に代入する。
def my_combination_table(N, M, v):
    if(len(v) < N + 1):
        l = N + 1 - len(v)
        tempo = [1] * l
        v.extend(tempo)

    for i in range(1, N + 1):
        v[i] = v[i - 1] * (N - (i - 1))
        v[i] %= M

        v[i] *= my_pow(i, M - 2, M)
        v[i] %= M

    return




#math.factorial で階乗は計算できる。
#math.gcd で gcd は計算できる。
#np.gcd.reduce(A) #(Aは配列) で、Aの全ての要素の gcd が計算できる。



H, W, K = (int(x) for x in input().split())
c = [input() for i in range(0, H)]

res = 0
for i in range(0, 2 ** H):
    for j in range(0, 2 ** W):
        cnt = 0
        for h in range(0, H):
            for w in range(0, W):
                if(c[h][w] == '#' and (1 << h & i) and (1 << w & j)): cnt += 1
        if(cnt == K): res += 1

print(res)
















