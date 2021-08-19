t = int(input())
for i in range(t):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    if n % 2:
        print('Second')
        continue
    enda = False
    for j in range(n // 2):
        if l[2 * j] != l[2 * j + 1]:
            print('First')
            enda = True
            break
    if enda:
        continue
    print('Second')
