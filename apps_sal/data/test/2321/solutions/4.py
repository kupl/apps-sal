for i in range(int(input())):
    x = int(input())
    y = input()
    print(min(y.index(">")if ">"in y else 10000000, y[::-1].index("<") if "<" in y else 100000000))
