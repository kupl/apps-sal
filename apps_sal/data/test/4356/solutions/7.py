

def main():
    n, m = list(map(int, input().split()))
    a = ['' for i in range(n)]
    b = ['' for i in range(m)]
    for i in range(n):
        a[i] = input()
    for i in range(m):
        b[i] = input()
    for i1 in range(n - m + 1):
        for i2 in range(n - m + 1):
            fl = True
            for j in range(m):
                for k in range(m):
                    if a[i1 + j][i2 + k] != b[j][k]:
                        fl = False
            if fl:
                print("Yes")
                return
    print("No")


def __starting_point():
    main()

__starting_point()
