from sys import stdin


def read():
    return list(map(int, stdin.readline().split()))


(n, k) = read()
print('NO' if '#' * k in stdin.readline() else 'YES')
