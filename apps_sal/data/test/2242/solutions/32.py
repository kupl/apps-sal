"""
Created on Mon Sep  7 00:38:11 2020

@author: liang
"""
'\n＜D - Multiple of 2019>\n【方針】\na = b(mod2019) => a - b は\u30002019の倍数\n余りが等しいグループの組み合わせの総数が解になる。\n既に2019の倍数であるものは単体で成立するため、[0]のカウントを一つあげておく\n\n\n＜累積和＞\n【計算量削減】\n大きな数を使わない\u3000⇒\u3000mod を使う\ntmp += 7 * 100000000  => 7 * ( 2019*N + α) => 7 * α\u3000と同じ\n\u3000\u3000⇒\u3000累乗(10**N) に  mod をかけると良い\n\n100000000 + γ => (2019*N + β) + γ => β + γ と同じ\n\u3000⇒\u3000累積和\u3000に\u3000mod をかけると良い\n \n for文で１文字ずつ足し算していくことで実装可能\n \n reversed() : 逆順に並べ替え\n reversed(input()) : 入力を逆順に取り出す\n \n'
S = input()
MOD = 2019
counter = [0] * 2019
counter[0] = 1
t = 1
tmp = 0
for i in reversed(S):
    tmp += int(i) * t
    tmp %= MOD
    t *= 10
    t %= MOD
    counter[tmp] += 1
ans = sum((i * (i - 1) // 2 for i in counter))
print(ans)
