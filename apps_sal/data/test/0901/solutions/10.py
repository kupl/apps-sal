def main():
    n,m = list(map(int,input().split()))

    for i in range(0,m):
        mk = True
        mp = set()
        ar = [int(i) for i in input().split()[1:]]
        #print(ar)
        for i in ar:
            if (-i) in mp:
                mk = False
                break
            mp.add(i)
        if mk:
            print("YES")
            return;
    print("NO")

def __starting_point():
    main()

__starting_point()
