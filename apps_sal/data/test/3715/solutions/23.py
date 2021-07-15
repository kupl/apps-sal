def __starting_point():
    MAX = 100
    n = int(input())
    num = list()
    for i in range(n + 1):
        num.append([0, 0, 0])
    line = str(input()).split()
    for i in range(n):
        if line[i] == '0':
            num[i + 1][0] = 1 + min(num[i])
            num[i + 1][1] = MAX
            num[i + 1][2] = MAX
        elif line[i] == '1':
            num[i + 1][0] = 1 + min(num[i])
            num[i + 1][1] = min(num[i][0], num[i][2])
            num[i + 1][2] = MAX
        elif line[i] == '2':
            num[i + 1][0] = 1 + min(num[i])
            num[i + 1][1] = MAX
            num[i + 1][2] = min(num[i][0], num[i][1])
        elif line[i] == '3':
            num[i + 1][0] = 1 + min(num[i])
            num[i + 1][1] = min(num[i][0], num[i][2])
            num[i + 1][2] = min(num[i][0], num[i][1])
    print(min(num[n]))

__starting_point()
