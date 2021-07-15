def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] < a[-1]:
        print("YES")
    else:
        print("NO")


def __starting_point():
    t = int(input())
    for i in range(t):
        main()

__starting_point()
