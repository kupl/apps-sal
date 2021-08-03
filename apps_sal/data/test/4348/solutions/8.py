n, k = map(int, input().split())
string = list(input())
test = []

if n != k:
    test = [(i, c) for i, c in enumerate(string)]
    test.sort(key=lambda a: a[1])

    test = test[k:]
    test.sort(key=lambda a: a[0])

    print(''.join([v for _, v in test]))
