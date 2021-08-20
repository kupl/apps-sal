import sys


def S():
    return sys.stdin.readline().rstrip()


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return map(int, sys.stdin.readline().rstrip().split())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def LS():
    return list(sys.stdin.readline().rstrip().split())


(a, b, c, d) = MI()
ans = 'No'
if a == b + c + d:
    ans = 'Yes'
elif b == a + c + d:
    ans = 'Yes'
elif c == a + b + d:
    ans = 'Yes'
elif d == a + b + c:
    ans = 'Yes'
elif a + b == c + d:
    ans = 'Yes'
elif a + c == b + d:
    ans = 'Yes'
elif a + d == b + c:
    ans = 'Yes'
print(ans)
