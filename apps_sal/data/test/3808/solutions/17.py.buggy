"""
NTC here
"""
from sys import setcheckinterval, stdin
setcheckinterval(1000)

# print("Case #{}: {} {}".format(i, n + m, n * m))


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


n = iin()
s = list(input())
ch1 = s.count('(')
if ch1 == n - ch1:
    a = []
    for i in range(n):
        if a:
            if s[i] == ')' and a[-1] == '(':
                a.pop()
            else:
                a.append(s[i])
        else:
            a.append(s[i])
    if len(a) == 2 or not a:
        print('Yes')
        return
print('No')
