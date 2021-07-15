#!/usr/bin/env python3

def rl(T=str):
    return list(map(T,input().split()))

def ok(a,d,x):
    for v in a:
        if v+x in d:
            return True
    return False


def try_one(a,d,x,y):
    def can_place(v):
        #print(v)
        #print(v+x,v-x,v+y,v-y)
        if a[0] <= v <= a[-1]:
            if (v + x in d or v - x in d) and \
               (v + y in d or v - y in d):
               return True

        return False;
    for v in a:
        for _ in [-x,+x,-y,+y]:
            if can_place(v+_):
                return v+_;

    return None

def main():
    n, l, x, y = rl(int)
    a = rl(int)
    d = set(a)

    if ok(a,d,x):
        if ok(a,d,y):
            print(0)
        else:
            print(1)
            print(y)
    else:
        if ok(a,d,y):
            print(1)
            print(x)
        else:
            p = try_one(a,d,x,y)
            if p is not None:
                print(1)
                print(p)
            else:
                print(2)
                print(x,y)

main()

