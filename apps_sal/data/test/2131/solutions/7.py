n = int(input())
dic = {}
for i in range(n):
    dic.update({i + 1: 0})
for i in range(n - 1):
    s = input().split()
    dic[int(s[0])] += 1
    dic[int(s[1])] += 1
cl = []
count1 = 0
count2 = 0
count3 = 0
for x in dic.keys():
    if dic[x] == 1:
        count1 += 1
        cl.append(x)
    elif dic[x] == 2:
        count2 += 1
    else:
        count3 += 1
        p = x
if count3 == 0:
    print('Yes')
    print(1)
    print('{} {}'.format(cl[0], cl[1]))
elif count3 == 1:
    print('Yes')
    print(count1)
    for i in range(1, n + 1):
        if i != p and dic[i] == 1:
            print('{} {}'.format(p, i))
else:
    print('No')
