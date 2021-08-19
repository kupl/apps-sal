# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:39:24 2020

@author: liang
"""
#from scipy.special import comb

counter = [0] * 2019
counter[0] = 1  # 0 = 0 (mod 2019)

S = input()
tmp = 0
"""
#大きい数を一気に掛けない
for i in range(1,len(S)+1):
    tmp += int(S[-i])*10**(i-1)    #スライスの方が早い（けど、漸化式的に累積和を出せ）
    #print(tmp%2019)
    tmp %= 2019                    #大きい数を割るな
    counter[tmp%2019] += 1

ans = 0
for i in range(2019):
    if counter[i] >= 2:
        #ans += comb(counter[i], 2, exact=True)
        ans += counter[i]*(counter[i]-1)//2
print(ans)
"""
MOD = 2019
# reversed(s) ?
t = 1
for i in range(1, len(S) + 1):
    tmp += int(S[-i]) * t
    #print("A", tmp)
    tmp %= MOD
    t *= 10
    #print("B", tmp)
    t %= MOD
    # print(tmp)
    counter[tmp] += 1

print((sum(i * (i - 1) // 2 for i in counter)))
