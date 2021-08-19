def lcm(a, b):
    sum = a + b
    large = a if a > b else b
    small = sum - large
    for i in range(1, small + 1):
        if (large * i) % small == 0:
            return large * i
    return None
    # dfs


n = int(input())
crush = list(map(int, input().split(" ")))
# crush = input().split(" ")
visited = [False] * n
graph_len = []

if sum(crush) != (n * (n + 1)) / 2:
    # not all nodes have incoming edges
    print('-1')
else:
    for i in range(n):
        if visited[i]:
            # visited nodes
            # print('visited already', i)
            continue
        idx = i
        len1 = 0
        while not visited[idx]:
            # not visited nodes
            # print('idx visiting', idx, crush[idx] - 1)
            visited[idx] = True
            idx = crush[idx] - 1  # convert values to zero index
            len1 += 1  # self loops 1. two node loop check
        len1 = (int)(len1 / 2) if len1 % 2 == 0 else len1
        if len1 not in graph_len:
            # we ll go for lcm. no point in having duplicates
            graph_len.append(len1)

# find lcm of elements in graph_len
    # print(graph_len)
    n1 = graph_len[0]
    for i in range(1, len(graph_len)):
        n2 = graph_len[i]
        n1 = lcm(n1, n2)
        # print('n1->', n1)
    print(n1)
