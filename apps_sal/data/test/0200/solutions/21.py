h1,h2 = list(map(int, input().split(" ")))
a,b = list(map(int, input().split(" ")))

def caterpillar(a,b,h1,h2):
    if h1 + 8*a >= h2:
        print(0)
    else:
        h = h1 + 8*a
        if 12*(a-b) <= 0:
            print(-1)
        else:
            c = h2-h
            d = 12*(a-b)
            print( (c // d) + (c%d > 0)*1)

caterpillar(a,b,h1,h2)

