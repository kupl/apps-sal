def calc_sum(num):
    ans = 0
    for i in range(len(str(num))):
        target = num % 10
        num //= 10
        ans += target
    return ans

def main():

    n, a, b = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        num = calc_sum(i)
        if a <= num <= b:
            ans += i
    print(ans)

def __starting_point():
    main()
__starting_point()
