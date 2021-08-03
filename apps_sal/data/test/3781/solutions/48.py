t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if n % 2 == 1:
        print('Second')

    else:
        D = {}
        for el in arr:
            if el not in D:
                D[el] = 1
            else:
                D[el] += 1

        ok = 1
        for key in D:
            if D[key] % 2 == 1:
                ok = 0

        if ok == 1:
            print('Second')
        else:
            print('First')
