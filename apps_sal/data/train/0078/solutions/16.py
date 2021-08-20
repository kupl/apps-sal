import sys


def input():
    return sys.stdin.readline().strip()


def print(x):
    return sys.stdout.write(f'{x}\n')


for t in range(int(input())):
    (r, c) = map(int, input().split())
    arr = [input() for i in range(r)]
    rarr = [0] * r
    carr = [0] * c
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                rarr[i] += 1
                carr[j] += 1
    ans = float('inf')
    for i in range(r):
        for j in range(c):
            s = rarr[i] + carr[j]
            if arr[i][j] == '.':
                ans = min(ans, s - 1)
            else:
                ans = min(ans, s)
    print(ans)
