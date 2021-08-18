import sys


for q in range(int(input())):
    n = int(sys.stdin.readline())
    data = []
    for i in range(n):
        data.append([int(j) for j in sys.stdin.readline().split()])
    dp = [[0, data[0][1], 2 * data[0][1]]]
    for i in range(1, n):
        a, b = data[i]
        lasta = data[i - 1][0]
        l = dp[-1]

        vals = [(lasta + j) for j in range(3)]
        ans = [0] * 3
        for j in range(3):
            w = a + j
            x = [l[k] for k in range(3) if lasta + k != w]
            ans[j] = j * b + min(x)
        dp.append(ans)
    print(min(dp[-1]))
