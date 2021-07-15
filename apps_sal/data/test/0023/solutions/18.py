def x(a,b):
    a.sort()
    #print('dsahhf    ',a,b)
    l = len(a)
    if len(a) < len(b):
        return(''.join(sorted(a,reverse = True)))
    elif l>len(b):
        #print(a,a[:-1])
        return '0' + x(a[1:],b)
    else:
        f = True
        if l ==0:return ''
        for i in range(l):
            if a[i]>b[i]:
                f = False
            elif a[i] < b[i]:break
        if not f:
            return -1
        a = list(a)
        a.sort(reverse = True)
        o = ''
        if b[0] in a:
            f = a.index(b[0])
            t = x(a[:f]+a[f+1:],b[1:])
            #print(t,a[:f]+a[f+1:],b[1:])
            f2 = -1
            if t == -1:
                m = '9'
                f2 = 0
                for i in range(l-1,-1,-1):
                    if a[i] >= b[0]:
                        break
                    m = a[i]
                    f2 = i
                #print(a,f2,m)
                #print(a[:f2],a[f2+1:])
                return m+''.join(a[:f2])+''.join(a[f2+1:])
            else:
                return b[0]+t
        else:
            m = '9'
            f2 = 0
            for i in range(l-1,-1,-1):
                if a[i] > b[0]:
                    break
                m = a[i]
                f2 = i
            #print(a,f2,m)
            #print(a[:f2],a[f2+1:])
            return m+''.join(a[:f2])+''.join(a[f2+1:])
a = input()
b = input()
print(int(x(list(sorted(a)),b)))

