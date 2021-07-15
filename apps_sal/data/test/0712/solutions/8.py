def main():
    a = input().split()
    n = int(a[0])
    p = float(a[1])
    t = int(a[2])
    z = [0.0] * (t+2)
    for i in range(t+2):
        z[i] = [0] * (n+2)
    l = 0.
    z[0][0] = 1.
    for i in range(t+1):
        for j in range(n+1):
            if j == n:
                z[i+1][j] += z[i][j]
            else:
                z[i+1][j+1] += z[i][j] * p
                z[i+1][j] += z[i][j] * (1-p)
    for j in range(n+1):
        l += z[t][j] * j
    print(l)
def __starting_point():
    main()

__starting_point()
