n = int(input())
dic = dict()
for i in range(n):
    s = input()
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1
print(max(dic.values()))

