def f(x):
    return (x > 1) + (x > 3)


def main():
    for _ in range(int(input())):
        x, y = list(map(int, input().split()))
        print("YES" if f(x) >= f(y) else "NO")


main()
