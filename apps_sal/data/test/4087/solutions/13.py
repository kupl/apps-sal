
def __starting_point():
    n = int(input())

    def dsum(n):
        ans = 0
        while n > 0:
            ans += n % 10
            n //= 10
        return ans
    while dsum(n) % 4 != 0:
        n += 1
    print(n)


__starting_point()
