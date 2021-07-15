def main():
    n,m=map(int,input().split())
    l=[tuple(map(int,input().split())) for _ in range(m)]
    py=sorted(l, key=lambda x: (x[0],x[1]))
    d={}
    i = 1
    prev=0
    for p,y in py:
        if prev != p:
            i = 1
            prev = p
        d[(p,y)] = "{:0>6}".format(p)+"{:0>6}".format(i)
        i += 1
    for x in l:
        print(d[x])

def __starting_point():
    main()
__starting_point()
