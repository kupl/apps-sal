for i in range(int(input()) + 1, 10000):
    if len(set(list(str(i)))) == 4:
        print(i)
        break
