def main():
    from sys import stdin, stdout
    for _ in range(int(stdin.readline())):
        n, m = list(map(int, stdin.readline().split()))
        n += 1
        m += 1
        div, mod = divmod(n, m)
        stdout.write(f'{(n ** 2 - div ** 2 * (m - mod) - (div + 1) ** 2 * mod) // 2}\n')


main()
