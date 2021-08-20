N = int(input())
d = []
for i in range(N):
    d.append(int(input()))
dic = {}
for i in range(N):
    if d[i] in dic:
        dic[d[i]] += 1
    else:
        dic[d[i]] = 1
print(len(dic))
