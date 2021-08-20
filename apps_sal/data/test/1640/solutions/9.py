"""
Created on Tue Dec 12 20:33:55 2017

@author: savit
"""
dic = {}
n = int(input())
sum1 = 0
a = list(map(int, input().split()))
for i in range(n - 1, -1, -1):
    try:
        dic[a[i]] += 1
    except:
        dic[a[i]] = 1
    sum1 += a[i] * (-n + 1 + 2 * i)
    try:
        sum1 -= dic[a[i] + 1]
    except:
        pass
    try:
        sum1 += dic[a[i] - 1]
    except:
        pass
print(sum1)
