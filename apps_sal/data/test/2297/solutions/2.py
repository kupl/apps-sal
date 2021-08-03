def main():
    def calc(x):
        if x & 1:
            return -x + calc(x - 1)
        return x // 2
    n = int(input())
    for i in range(n):
        a, b = list(map(int, input().split()))
        print(calc(b) - calc(a - 1))


main()
