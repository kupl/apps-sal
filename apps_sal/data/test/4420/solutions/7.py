def main():
    t = int(input())
    for i in range(t):
        solve()

def solve():
    x, y, n = list(map(int, input().split(" ")))

    if n % x >= y:
        print((n // x) * x + y)
    else:
        print((n // x - 1) * x + y)

main()


