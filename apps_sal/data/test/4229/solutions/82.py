from sys import stdin, stdout


def main():
    n = int(stdin.readline().rstrip())
    ans = 0
    for number in range(1, n + 1):
        if number % 3 != 0 and number % 5 != 0:
            ans = ans + number
    stdout.write(str(ans))
    stdout.write('\n')


main()
