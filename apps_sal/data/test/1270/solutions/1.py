def main():
    n = int(input())
    if n % 2 == 0:
        count = n // 2
        print(count)
        print(' '.join(['2'] * count))
    else:
        count = 1 + (n - 3) // 2
        print(count)
        print(' '.join(['3'] + ['2'] * (count - 1)))

main()

