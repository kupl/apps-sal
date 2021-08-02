def main():
    count = 0
    n, x = map(int, input().split())
    for i in range(1, n + 1):
        if x % i == 0:
            if x // i <= n:
                count += 1
    print(count)


main()
