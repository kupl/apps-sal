import sys
def work(c,c1, s):
    maxlast, maxfirst,minlast,minfirst = 0,0,0,0
    max = 0
    min = 0
    y = 0
    for i in range(len(s)):
        if s[i] == c:
            y += 1
        elif s[i] == c1:
            y -=1

        if max < y:
            maxfirst,maxlast = i,i
            max = y
        elif max ==y :
            maxlast = i

        if y < min:
            minlast,minfirst =i,i
            min = y
        elif min == y:
            minlast = i
    flag = 0
    if (maxlast<minfirst or maxfirst>minlast) and max-min > 1:
        flag = 1
    return  max-min+1,flag

count = 0
for line in sys.stdin:
    if count == 0:
        n = int(line.strip().split(' ')[0])
        #k = int(line.strip().split(' ')[1])
        #m = int(line.strip().split(' ')[2])
        count += 1
        continue
    s = line.strip()
    flag,flag1 =0,0
    n,flag = work('W','S', s)
    m,flag1 = work('A', 'D', s)

    res = n * m
    if flag1 and flag:
        res = min(n*(m-1),m*(n-1))
    elif flag:
        res = m*(n-1)
    elif flag1:
        res = (m-1)*n
    print(res)
