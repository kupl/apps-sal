n = int(input())
dic = {}
for i in range(n):
    s = input()
    if not s in dic:
        dic[s] = 1
    else:
        dic[s] += 1
max_val = max(dic.values())
a = sorted([i for (i, k) in dic.items() if k == max_val])
for i in a:
    print(i)
