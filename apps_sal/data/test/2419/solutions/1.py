for tcase in range(int(input())):
    a, b = list(map(int, input().split()))
    if a == b:
        print(0)
    else:
        delta = abs(b - a)
        i = 1
        sm = 0
        while sm < delta:
            sm += i
            i += 1
        while (sm % 2) != (delta % 2):
            sm += i
            i += 1
        print(i - 1)
