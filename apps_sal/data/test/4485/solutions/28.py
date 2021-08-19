n, m = list(map(int, input().split()))
#a_to = []
#a_from = []
dic = {}
isOK = False
for i in range(m):
    a, b = list(map(int, input().split()))
    if a in [1, n]:
        dic.setdefault(b, 0)
        dic[b] += 1
        if dic[b] == 2:
            isOK = True
            break
    elif b in [1, n]:
        dic.setdefault(a, 0)
        dic[a] += 1
        if dic[a] == 2:
            isOK = True
            break
#    if a==1:
#        a_to.append(b)
#    if b==1:
#        a_to.append(a)
#    if a==n:
#        a_from.append(b)
#    if b==n:
#        a_from.append(a)

# for j in range(len(a_to)):
#    if a_to[j] in a_from:
#        isOK = True
#        break
# print(a_to)
# print(a_from)
if isOK:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
