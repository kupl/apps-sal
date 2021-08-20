import math
from functools import reduce
n = int(input())
lis = [int(x) for x in input().split()]
dic = {0: 0, 1: 0, 2: 0}
max_num = 2
for (j, i) in enumerate(lis):
    temp_dic = {}
    lis = set()
    for k in range(1, math.ceil(math.sqrt(i)) + 2):
        if i % k == 0:
            lis.add(k)
            if i % i // k == 0:
                lis.add(i // k)
    for k in lis:
        if k - 1 in dic:
            temp_dic[k] = (temp_dic.get(k, 0) + dic.get(k - 1)) % 1000000007
    for k in list(temp_dic.keys()):
        dic[k] = dic.get(k, 0) + temp_dic[k]
    dic[1] += 1
su = 0
for i in list(dic.keys()):
    su += dic[i] % 1000000007
print(su % 1000000007)
