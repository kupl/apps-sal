from sys import stdin, exit
input = stdin.readline


def i():
    return input()


def ii():
    return int(input())


def iis():
    return list(map(int, input().split()))


def liis():
    return list(map(int, input().split()))


def print_array(a):
    print(' '.join(map(str, a)))


t = ii()
for _ in range(t):
    (a, b) = iis()
    print(a + b)
