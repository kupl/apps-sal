n = int(input())
dic = {}
for i in range(n):
    text = input().split()
    nam = text[0]
    if nam not in dic:
        dic[nam] = set()
    for elem in text[2:]:
        dic[nam].add(elem)
# print(dic)
print(len(dic))
for nam, s in list(dic.items()):
    ls = []
    for e in s:
        add = True
        l = len(e)
        for j in s:
            if j != e and j[-l:] == e:
                add = False
                break
        if add:
            ls.append(e)
    print(nam, len(ls), *ls)
