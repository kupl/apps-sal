__author__ = 'PrimuS'
s1 = input().strip("\n")
s2 = input().strip("\n")
n = int(input())
d1 = {}
d2 = {}

for i in range(n):
    ss = input().split()
    t = int(ss[0])
    x = int(ss[2])
    ss[3].strip("\n")
    if ss[1] == 'h':
        if x in d1 and d1[x] == 1:
            print(s1, x, t)
            d1[x] = 2
        elif x not in d1:
            if ss[3] == 'r':
                print(s1, x,t)
                d1[x] = 2
            else:
                d1[x] = 1
    else:
        if x in d2 and d2[x] == 1:
            print(s2, x, t)
            d2[x] = 2
        elif x not in d2:
            if ss[3] == 'r':
                print(s2, x, t)
                d2[x] = 2
            else:
                d2[x] = 1
