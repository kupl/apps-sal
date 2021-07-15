t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    table = [[0 for i in range(n)] for j in range(n)]
    if k % n == 0:
        print(0)
    else:
        print(2)
    i = 0
    j = 0
    bias = 0
    for __ in range(k):
        table[i][j % n] = 1
        i += 1
        j += 1
        if i >= n:
            bias += 1
            i = 0
            j = bias
    for i in table:
        print(''.join(map(str, i)))
