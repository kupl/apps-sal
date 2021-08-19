q = int(input())
dic = {}
for i in range(q):
    (a, b) = input().split()
    used = False
    for i in list(dic.keys()):
        if a == dic[i]:
            used = True
            dic[i] = b
    if not used:
        dic[a] = b
print(len(dic))
for i in list(dic.keys()):
    print(i, dic[i])
