def main():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split()))
        moves = 0
        diff = abs(a - b)
        x = diff // 5
        moves += x
        diff -= (5 * x)
        x = diff // 2
        moves += x
        diff -= (2 * x)
        x = diff
        moves += x

        print(moves)


main()
