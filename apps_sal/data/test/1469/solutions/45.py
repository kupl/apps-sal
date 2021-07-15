L=int(input())

ans = []
m = 0
add = -1
mask = 0xffffff
for i in range(24):
    mask >>= 1
    d = 24 - i - 1
    if ((~mask) & L) != 0:
        if add == -1:
            n = d+1
            add = 1 << d
            b = 1
            # [0, 2^d) の範囲
            for i in range(1,d+1):
                ans.append(str(i) + " " + str(i+1) + " 0")
                ans.append(str(i) + " " + str(i+1) + " " + str(b))
                b *= 2
                m += 2
        else :
            ans.append(str(d+1) + " " + str(n) + " " + str(add))
            add += (1 << d)
            m += 1
        L &= mask
#    print(" ",d,L,mask)
print((n,m))
for i in ans:
    print(i)


