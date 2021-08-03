a = int(input())
l = []
for j in range(a):
    start = 1
    end = 1
    h = list(map(int, input().split()))
    n = h[0]
    p = h[1]
    for i in range(2 * n + p):
        if (end + 1 > n):
            start += 1
            end = start + 1
        else:
            end += 1
        print(start, end)
