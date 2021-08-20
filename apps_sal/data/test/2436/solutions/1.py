import sys


def pprint(s):
    return print(' '.join(map(str, s)))


def input():
    return sys.stdin.readline().strip()


ipnut = input
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    a.sort()
    for i in range(n):
        if i + 1 >= a[i]:
            ans = i + 2
    print(ans)
