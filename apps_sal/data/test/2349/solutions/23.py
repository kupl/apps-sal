for i in range(int(input())):
    n = int(input())
    b = [i for i in range(1, int(n**(1 / 2) + 1))]
    r = [str(m) for m in sorted(list(set(b + [n // i for i in b])))]
    print(len(r) + 1)
    print(0, ' '.join([str(m) for m in sorted(list(set(b + [n // i for i in b])))]))
