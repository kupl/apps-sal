N = int(input())

for i in range(N):
    a = list(map(int, input().split()))
    c = 0
    for i in range(a[0]):
        if c == 2 * a[0] + a[1]:
            break
        for j in range(i + 1, a[0]):
            if c == 2 * a[0] + a[1]:
                break
            print(i + 1, j + 1)
            c = c + 1
