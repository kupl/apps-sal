from sys import stdin, stdout


def main():
    s = stdin.readline().rstrip()
    res = 0
    for elem in s:
        if int(elem) % 4 == 0:
            res += 1
    for i in range(len(s) - 1):
        if int(s[i:i + 2]) % 4 == 0:
            res += i + 1
    stdout.write(str(res))


main()
