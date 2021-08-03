from sys import stdin, stdout


def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)


a, b, time = map(int, stdin.readline().split())
stdout.write(str(time // (a * b // gcd(a, b))))
