def main():
    n = int(input())
    s = int(input())

    def check(a, i):
        ans = 0
        while a:
            ans += a % i
            a //= i
        return ans
    for i in range(2, int(n ** 0.5) + 2):
        if check(n, i) == s:
            print(i)
            return 0
    for i in range(int(n ** 0.5), 0, -1):
        if (n - s) % i == 0:
            b = (n - s) // i + 1
            x = s - i
            if x < 0:
                continue
            if b > x:
                print(b)
                return 0
    if n == s:
        print(n + 1)
    else:
        print(-1)


main()
