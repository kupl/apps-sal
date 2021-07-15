def main():
    X, Y, Z = list(map(int, input().split()))
    rest = X - Z
    c = 0
    while rest > 0:
        rest = rest - Y - Z
        if rest < 0:
            print(c)
            return
        elif rest == 0:
            print((c+1))
            return
        else:
            c += 1
main()

