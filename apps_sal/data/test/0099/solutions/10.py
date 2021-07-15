def solve():
    b1, q, l, m = map(int, input().split())
    bads = set(map(int, input().split()))
    
    terms = set()
    
    if b1 == 0:
        if 0 not in bads:
            print("inf")
        else:
            print(0)
    elif q == 0:
        if abs(b1) > l:
            print(0)
        else:
            if 0 not in bads:
                print("inf")
            else:
                if b1 not in bads:
                    print(1)
                else:
                    print(0)
    elif q == 1:
        if abs(b1) <= l:
            if b1 not in bads:
                print("inf")
            else:
                print(0)
        else:
            print(0)
    elif q == -1:
        if abs(b1) <= l:
            if b1 not in bads or -b1 not in bads:
                print("inf")
            else:
                print(0)
        else:
            print(0)
    else:
        b = b1
        while abs(b) <= l:
            terms.add(b)
            b *= q
        print(len(terms) - len(terms.intersection(bads)))

solve()
