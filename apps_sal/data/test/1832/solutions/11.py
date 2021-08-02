maxs = 190
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(j) for j in input().split()]
    ans = [0] * (n + 1)
    ans[0] = 'a' * maxs
    for i in range(1, n + 1):
        num = arr[i - 1]
        current = ''
        for j in range(num):
            current += ans[i - 1][j]
        if ans[i - 1][num] == 'a':
            current += 'b'
        else:
            current += 'a'

        for j in range(num + 1, maxs):
            current += current[j - 1]

        ans[i] = current
    print(*ans, sep='\n')
