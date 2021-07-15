def mi():
    return map(int, input().split())

'''
3
6
4 5 1 3 2 6
5
5 3 1 2 4
4
1 4 3 2
3
6
4 5 1 3 2 6
5
5 3 1 2 4
4
1 4 3 2
'''
for _ in range(int(input())):
    n = int(input())
    a = list(mi())
    t = a.index(1)
    dist = [0]*(n+1)
    dic = [0]*n
    for i in range(n):
        dist[a[i]] = abs(t-i)
        dic[i] = [a[i], i]
    dic.sort()
    lm = dic[0][1]
    rm = dic[0][1]
    print (1, end = '')
    for i in range(1, n):
        if (dic[i][1]<lm):
            lm = dic[i][1]
        if (dic[i][1]>rm):
            rm = dic[i][1]
        if rm-lm<i+1:
            print (1, end = '')
        else:
            print (0, end = '')
    print()
