

def __starting_point():
    length, target = [int(i) for i in input().strip().split()]

    array = [1000000000000] + [int(i) for i in input().strip().split()]
    num_dict = dict()
    up, down, pre, dp = [], [], dict(), [0 for i in range(length + 1)]
    index = 0
    ans = 0
    for i in range(length + 1):
        if array[i] == target:
            index += 1
            up.append(index)
        else:
            up.append(index)
    index = 0
    for i in range(length, -1, -1):
        if array[i] == target:
            index += 1
            down.append(index)
        else:
            down.append(index)
    down.reverse()
    down.append(0)

    for i in range(1, length + 1):
        if array[i] not in pre:
            pre[array[i]] = 0
        dp[i] = max(up[i - 1] + 1, dp[pre[array[i]]] + 1)
        pre[array[i]] = i
        # print(i)
        ans = max(ans, dp[i] + down[i + 1])
    print(ans)


__starting_point()
