dic = {}
s = int(input())
i = 0
while (i < s):
    x = input()
    h = x.split()
    if h[0] in dic:
        dic[h[1]] = dic.pop(h[0])
    else:
        dic[h[1]] = h[0]
    i += 1
print(len(dic))
for x in dic:
    print(dic[x] + " " + x)
