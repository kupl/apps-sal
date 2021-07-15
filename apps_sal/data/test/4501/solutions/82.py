from collections import defaultdict
n, a = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
x = list(map(lambda x:x - a, x))
dic = defaultdict(int)
dic[0] = 1
for i in x:
    for j, k in list(dic.items()):
        dic[j + i] = dic.get(j + i, 0) + k
print(dic[0] - 1)
