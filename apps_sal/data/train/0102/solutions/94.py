for i in range(int(input())):
    n = input()
    counter = (len(n) - 1) * 9
    for i in range(1, 10):
        if (int(str(i) * len(n)) <= int(n)):
            counter += 1
    print(counter)

