w, m = list(map(int, input().split(' ')))
f = 0
if (w == 2):
    print("YES")
else:
    st = 1
    while (f == 0):
        if (m % (st * w) != 0):
            if ((m - st) % (st * w) == 0):
                m -= st
            else:
                if ((m + st) % (st * w) == 0):
                    m += st  
                else:
                    print("NO")
                    f = 1
            if (m == 0):
                print("YES")
                f = 1                    
        st *= w

