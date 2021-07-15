for _ in range(int(input())):
    n = int(input())
    s = input()
    blocks = [[s[0], 1]]
    for i in range(1, n):
        if s[i] == blocks[-1][0]:
            blocks[-1][1] += 1
        else:
            blocks += [[s[i], 1]]
    one = 0
    zero = 0
    for i in range(len(blocks)):
        if blocks[i][0] == '0':
            zero += blocks[i][1] - 1
        else:
            one += blocks[i][1] - 1
    print(max(one, zero))
