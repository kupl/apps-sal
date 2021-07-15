n = int(input())
s = [input() for i in range(n)]
dic = {}
for i in range(n):
    if s[i] in dic.keys():
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1
max1 = max(dic.values())
ans = []
for keys in dic.keys():
    if dic[keys] == max1:
        ans.append(keys)
ans.sort()
for i in ans:
    print(i)
