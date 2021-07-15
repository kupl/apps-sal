def main():
    x, n, m = list(map(int, input().split()))
    while x > 20 and n > 0:
        n -= 1
        x = x//2 + 10
    if x > m * 10:
        print("NO")
    else:
        print("YES")


def __starting_point():
    t = int(input())
    for i in range(t):
        main()

__starting_point()
