def main():
    w1,h1,w2,h2 = list(map(int, input().split()))
    s = max(w1,w2)
    u = h1+h2
    print(2*(s+u)+4)



def __starting_point():
    main()

__starting_point()
