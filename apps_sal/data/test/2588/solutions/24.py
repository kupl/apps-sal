def main():

    def solve():
        (n, a, b) = map(int, input().split())
        ss = input()
        cost = 0
        for i in range(n):
            if ss[i] == '1':
                last = i
                cost += a * (i + 1) + b * i
                break
        else:
            print(a * n + b * (n + 1))
            return
        for i in range(last, n):
            if ss[i] == '1' or ss[i - 1] == '1':
                high = (i - last) * (a + 2 * b)
                low = (i - last) * (a + b) + a * 2 + b
                cost += min(high, low)
                last = i
        cost += (n + 1 - last) * (a + b) + b
        print(cost)
    q = int(input())
    for _ in range(q):
        solve()


def __starting_point():
    main()


__starting_point()
