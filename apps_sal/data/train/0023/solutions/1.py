'''
Created on 2019. 9. 21.

@author: kkhh88
'''
#q = int(input())
#x, y = map(int,input().split(' '))

q = int(input())
for _ in range(q):
    n = int(input())
    lr = []
    for i in range(n):
        lr.append(list(map(int, input().split(' '))))

    lr.sort(key=lambda x: x[1], reverse=True)
    lr.sort(key=lambda x: x[0])

    cnt = [0] * n
    for i in range(n):
        if lr[i][0] > i:
            if lr[i][0] - i > cnt[lr[i][0]]:
                cnt[lr[i][0]] = lr[i][0] - i

    i = n - 1
    tmp = 0
    ans = 0
    lst = []
    while i >= 0:
        if i > 0 and lr[i][0] == lr[i - 1][0]:
            lst.append(lr[i][1])
            i = i - 1
        else:
            lst.append(lr[i][1])
            if cnt[lr[i][0]] > tmp:
                lst.sort()
                for _ in range(tmp, cnt[lr[i][0]]):
                    ans = ans + lst.pop(0)
                tmp = cnt[lr[i][0]]
            i = i - 1
    #print (cnt, lr)
    print(ans)
