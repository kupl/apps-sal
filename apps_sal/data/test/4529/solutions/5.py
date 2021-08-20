for _ in range(int(input())):
    n = int(input())
    ar = list(input())
    (left, right) = (0, 0)
    kek = [[0, 0, 0]]
    for i in range(n):
        elem = ar[i]
        if elem == 'L':
            left -= 1
        elif elem == 'R':
            left += 1
        elif elem == 'U':
            right += 1
        else:
            right -= 1
        kek.append([left, right, i + 1])
    kek.sort()
    ans = 10 ** 9
    (a, b) = (-1, -1)
    for i in range(n + 1):
        if kek[i][0] == kek[i - 1][0] and kek[i][1] == kek[i - 1][1] and (kek[i][2] - kek[i - 1][2] < ans):
            ans = kek[i][2] - kek[i - 1][2]
            (a, b) = (kek[i - 1][2] + 1, kek[i][2])
    if a == b == -1:
        print(-1)
    else:
        print(a, b)
