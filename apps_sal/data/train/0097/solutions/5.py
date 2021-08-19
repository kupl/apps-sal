for _ in range(int(input())):
    (a, b) = input().split()
    a = list(a)
    for i in range(len(a) - 1):
        j = min((i for i in range(i + 1, len(a))), key=lambda x: (a[x], -x))
        if a[i] > a[j]:
            (a[i], a[j]) = (a[j], a[i])
            break
    a = ''.join(a)
    if a < b:
        print(a)
    else:
        print('---')
