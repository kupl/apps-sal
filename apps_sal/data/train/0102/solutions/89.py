def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = str(n)
        l = len(s)
        if(l == 1):
            print(n)
            continue
        c = 9 * (l - 1)
        f = int(s[0] * l)
        if(n >= f):
            print(c + (f % 10))
        else:
            print(c + (f % 10) - 1)


main()
