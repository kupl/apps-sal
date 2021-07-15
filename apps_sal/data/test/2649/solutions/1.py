

def main():
    n = int(input())
    z = [[], []]
    for i in range(n):
        x, y = list(map(int, input().split()))
        z[0].append(x + y)
        z[1].append(x - y)
    z[0] = sorted(z[0])
    z[1] = sorted(z[1])
    print((max(z[0][-1] - z[0][0], z[1][-1] - z[1][0])))



def __starting_point():
    main()

__starting_point()
