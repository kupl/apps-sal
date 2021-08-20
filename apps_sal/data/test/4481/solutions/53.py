from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for i in range(n):
    dic[input()] += 1
tmp = [(key, value) for (key, value) in dic.items()]
tmp.sort(key=lambda x: (x[1], x[0]))
m = tmp[-1][1]
for i in range(len(dic)):
    if tmp[i][1] == m:
        print(tmp[i][0])
