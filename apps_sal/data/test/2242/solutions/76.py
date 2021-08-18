"""
Created on Sun Sep  6 23:39:24 2020

@author: liang
"""

counter = [0] * 2019
counter[0] = 1

S = input()
tmp = 0
"""
for i in range(1,len(S)+1):
    tmp += int(S[-i])*10**(i-1)    
    tmp %= 2019                    
    counter[tmp%2019] += 1

ans = 0
for i in range(2019):
    if counter[i] >= 2:
        ans += counter[i]*(counter[i]-1)//2
print(ans)
"""
MOD = 2019
t = 1
for i in range(1, len(S) + 1):
    tmp += int(S[-i]) * t
    tmp %= MOD
    t *= 10
    t %= MOD
    counter[tmp] += 1

print((sum(i * (i - 1) // 2 for i in counter)))
