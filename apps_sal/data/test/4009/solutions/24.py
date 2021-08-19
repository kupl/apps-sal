from sys import stdin


def input():
    return stdin.readline()[:-1]


(n, x, y) = list(map(int, input().split()))
s = input()
ones = s[-1 * x:].count('1') - (s[-1 * y - 1] == '1') + (s[-1 * y - 1] == '0')
print(ones)
