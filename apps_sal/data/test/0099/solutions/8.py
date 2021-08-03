a, r, l, m = list(map(int, input().split()))
_l = list(map(int, input().split()))
s = set(_l)
if(abs(a) > l):
    print(0)
    return
if(a == 0):
    if(0 in s):
        print(0)
        return
    else:
        print("inf")
        return
if(r == 0):
    if(a == 0):
        if(0 in s):
            print(0)
            return
        else:
            print("inf")
            return
    else:
        if(a not in s):
            if(abs(a) <= l):
                if(0 in s):
                    print(1)
                    return
                else:
                    print("inf")
                    return
            else:
                print(0)
                return
        else:
            if(0 in s):
                print(0)
                return
            else:
                print("inf")
                return
if(r == 1):
    if(a in s or abs(a) > l):
        print(0)
        return
    else:
        print("inf")
        return
if(r == -1):
    if(a in s):
        if(0 - a in s):
            print(0)
            return
        else:
            if(abs(a) <= l):
                print("inf")
                return
            else:
                print(0)
                return
    else:
        if(abs(a) <= l):
            print("inf")
            return
        else:
            print(0)
            return
tot = 0
while(abs(a) <= l):
    if(a not in s):
        tot += 1
    a *= r
print(tot)
