for _ in range(int(input())):
    am = int(input())
    arr = list(map(int, input().split()))
    if len(set(arr)) == 1:
        print('NO')
        continue
    print('YES')
    f = (0, arr[0])
    s = (0, 0)
    for i in range(am):
        if arr[i] != f[1]:
            s = (i, arr[i])
    print(f[0] + 1, s[0] + 1)
    for i in range(am):
        if i != f[0] and i != s[0]:
            if arr[i] == f[1]:
                print(i + 1, s[0] + 1)
            else:
                print(i + 1, f[0] + 1)
