def f():
    sizes = input().split(' ')
    (n, m) = (int(sizes[0]), int(sizes[1]))
    permStr = input().split(' ')
    pairsStr = [input() for i in range(m)]
    indexes = [0 for i in range(n + 1)]
    for i in range(n):
        indexes[int(permStr[i])] = i + 1
    lowerNums = [0 for i in range(n + 1)]
    for i in range(m):
        pair = pairsStr[i].split(' ')
        (a, b) = (indexes[int(pair[0])], indexes[int(pair[1])])
        if a < b:
            l = a
            h = b
        else:
            l = b
            h = a
        if l > lowerNums[h]:
            lowerNums[h] = l
    counter = 0
    left = 0
    for i in range(1, n + 1):
        candidate = lowerNums[i]
        if candidate > left:
            r = i - 1 - left
            q = i - 1 - candidate
            counter += (r * (r - 1) - q * (q - 1)) // 2
            left = candidate
    r = i - left
    counter += r * (r - 1) // 2
    print(counter + n)


f()
