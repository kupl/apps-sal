N, M = list(map(int, input().split()))
li = [0] * M

for i in range(M):
    P, Y = list(map(int, input().split()))
    li[i] = (P, Y)

li2 = sorted(li)

s = '000000'
tmp = 0
cnt = 1
dic = {}
for i in li2:
    if tmp == i[0]:
        cnt += 1
    else:
        cnt = 1
        tmp = i[0]

    s1 = s[0:6 - len(str(i[0]))] + str(i[0])
    s2 = s[0:6 - len(str(cnt))] + str(cnt)
    s3 = s1 + s2
    dic[i] = s3

for i in li:
    print((dic[i]))
