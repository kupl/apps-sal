import sys
3


def input():
    return sys.stdin.readline().strip()


n = int(input())
w = [int(x) for x in input().split()]
print(min((abs(sum(w[:i]) - sum(w[i:])) for i in range(n))))
