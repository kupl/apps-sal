import sys
import socket
hostname = socket.gethostname()
if hostname == 'F451C':
    sys.stdin = open('f1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


M = 10 ** 9 + 7
f = [1] * (2 * 10 ** 6 + 4)
for i in range(1, 2 * 10 ** 6 + 3):
    f[i] = f[i - 1] * i
    f[i] %= M


def g(r, s):
    res = 1
    frs = f[r + s + 2]
    fs = f[s + 1]
    fr = f[r + 1]
    res *= pow(fr, M - 2, M)
    res *= pow(fs, M - 2, M)
    res *= frs
    res %= M
    return res


def main():
    (r1, c1, r2, c2) = read_int_list()
    res = 0
    res += g(r2, c2) - g(r2, c1 - 1) - g(r1 - 1, c2) + g(r1 - 1, c1 - 1)
    res %= M
    print(res)


main()
