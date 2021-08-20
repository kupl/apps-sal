from sys import stdin, stdout
import math


def main():
    k = int(stdin.readline().rstrip())
    ans = 0
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            ab = math.gcd(a, b)
            for c in range(1, k + 1):
                ans = ans + math.gcd(ab, c)
    stdout.write(str(ans))
    stdout.write('\n')


main()
