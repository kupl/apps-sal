import sys
fast_reader = sys.stdin.readline
fast_writer = sys.stdout.write


def input():
    return fast_reader().strip()


def print(*argv):
    fast_writer(' '.join((str(i) for i in argv)))
    fast_writer('\n')


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 'YES'
    for i in range(n - 1):
        if l[i + 1] - l[i] > 1:
            ans = 'NO'
            break
    print(ans)
