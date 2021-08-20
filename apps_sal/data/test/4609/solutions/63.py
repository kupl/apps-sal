N = int(input())
dic = {}
for i in range(N):
    a = int(input())
    if a not in dic:
        dic[a] = 1
    else:
        del dic[a]
print(len(dic))
