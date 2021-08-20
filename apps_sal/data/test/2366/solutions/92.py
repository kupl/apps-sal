import collections
n = int(input())
a = list(map(int, input().split()))
dic = collections.Counter(a)
total = 0
for x in list(dic.values()):
    total += x * (x - 1) // 2
for y in range(n):
    b = a[y]
    lost = dic[b] * (dic[b] - 1) // 2 - (dic[b] - 1) * (dic[b] - 2) // 2
    print(total - lost)
