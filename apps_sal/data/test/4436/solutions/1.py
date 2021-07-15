def Fenjie(n):
    k = {}
    if (n == 1):
        return {}
    a = 2
    while (n >= 2):
        b = n%a
        if (a*a > n):
            if (n in k):
                k[n] += 1
            else:
                k[n] = 1
            break
        if (b == 0):
            if (a in k):
                k[a] += 1
            else:
                k[a] = 1
            n = n//a
        else:
            a += 1
    return k

n = int(input())
for _ in range(n):
    m = int(input())
    k = Fenjie(m)
    s = 0
    le = len(k)
    l = [i for i in k]
    if (le >= 3):
        print("YES")
        flag = 0
        print(l[0], l[1], m//l[0]//l[1])
    elif (le==2):
        if (k[l[0]]+k[l[1]] >= 4):
            print("YES")
            print(l[0], l[1], m//l[0]//l[1])
        else:
            print("NO")
    else:
        if (k[l[0]] >= 6):
            print("YES")
            print(l[0], l[0]*l[0], m//l[0]//l[0]//l[0])
        else:
            print("NO")
