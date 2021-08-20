"""
Created on Sun Sep  6 23:39:24 2020

@author: liang
"""
counter = [0] * 2019
counter[0] = 1
S = input()
tmp = 0
'\n#大きい数を一気に掛けない\nfor i in range(1,len(S)+1):\n    tmp += int(S[-i])*10**(i-1)    #スライスの方が早い（けど、漸化式的に累積和を出せ）\n    #print(tmp%2019)\n    tmp %= 2019                    #大きい数を割るな\n    counter[tmp%2019] += 1\n\nans = 0\nfor i in range(2019):\n    if counter[i] >= 2:\n        #ans += comb(counter[i], 2, exact=True)\n        ans += counter[i]*(counter[i]-1)//2\nprint(ans)\n'
MOD = 2019
t = 1
for i in range(1, len(S) + 1):
    tmp += int(S[-i]) * t
    tmp %= MOD
    t *= 10
    t %= MOD
    counter[tmp] += 1
print(sum((i * (i - 1) // 2 for i in counter)))
