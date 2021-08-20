for _ in range(int(input())):
    s = input()
    n = len(s)
    data = [0] * n
    for i in range(n):
        if s[i] == '+':
            data[i] = 1
        else:
            data[i] = -1
    for i in range(1, n):
        data[i] += data[i - 1]
    data = [-data[i] for i in range(n)]
    for i in range(1, n):
        data[i] = max(data[i], data[i - 1])
    res = 0
    val = 0
    id = 0
    while id < n:
        if data[id] > val:
            res += id + 1
            val += 1
        else:
            id += 1
    res += id
    print(res)
