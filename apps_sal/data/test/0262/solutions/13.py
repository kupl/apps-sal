def check(a, t):
    n = len(a)
    for i in range(n):
        if sum(a[i]) != t:
            return False
    for j in range(n):
        if sum((a[i][j] for i in range(n))) != t:
            return False
    return sum((a[i][i] for i in range(n))) == sum((a[i][-i - 1] for i in range(n))) == t


def main():
    try:
        while True:
            n = int(input())
            a = [list(map(int, input().split())) for i in range(n)]
            if n == 1:
                print(1)
            else:
                try:
                    j = a[0].index(0)
                    i = 0
                    t = sum(a[1])
                    x = t - sum(a[0])
                except ValueError:
                    t = sum(a[0])
                    for i in range(1, n):
                        try:
                            j = a[i].index(0)
                            x = t - sum(a[i])
                            break
                        except ValueError:
                            pass
                a[i][j] = x
                print(x if x > 0 and check(a, t) else -1)
    except EOFError:
        pass


main()
