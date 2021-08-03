def main():
    import sys
    input = sys.stdin.readline

    def solve():
        n, a, b = map(int, input().split())
        s = input()

        arr = [0] * (n + 1)
        for i in range(1, n):
            if s[i] == '1' or s[i - 1] == '1':
                arr[i] = 1

        cnts = []
        cnt = 1
        for i in range(1, n + 1):
            if arr[i] != arr[i - 1]:
                cnts.append(cnt)
                cnt = 1
            else:
                cnt += 1
        cnts.append(cnt)

        l = len(cnts)
        cost = n * a + (l - 1) * a + (n + 1) * b + sum(cnts[1:l:2]) * b
        for i in range(2, l - 2, 2):
            now = 2 * a + cnts[i] * b
            new = cnts[i] * 2 * b
            if new < now:
                cost += new - now

        print(cost)

    for _ in range(int(input())):
        solve()

    return 0


main()
