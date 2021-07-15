lr = input().split()
l,r = [int(x) for x in lr]

if l == r:
    print(0)
    
else:
    a,b = list(bin(l)[2:]), list(bin(r)[2:])
    if len(a) == len(b):
        i = 0
        while a[i] == b[i]:
            i+=1
        left = '1'*(len(a)-i)
        print(int(left,2))
    elif len(a) > len(b):
        left = '1'*(len(a))
        print(int(left,2))
    else:
        left = '1'*(len(b))
        print(int(left,2))
