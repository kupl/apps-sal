

def main():
    n, m = map(int, input().split())
    if n == 2 and m == 2:
        print("YES")
    else:
        if n == 1 or m == 1:
            print("YES")
        else:
            print("NO")


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
