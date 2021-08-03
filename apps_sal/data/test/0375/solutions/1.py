import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

can1 = 1
can2 = 1
ft = -1
for i in range(n):
    if s[i] != t[i]:
        ft = i
        break


def check(ft, s, t):
    lt = n - 1
    for i in range(ft, n - 1):
        if s[i] != t[i + 1]:
            lt = i
            break
    for i in range(lt + 1, n):
        if s[i] != t[i]:
            return 0
    return 1


print(check(ft, s, t) + check(ft, t, s))
