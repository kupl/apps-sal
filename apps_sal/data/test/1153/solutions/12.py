# import sys
# from io import StringIO
#
# sys.stdin = StringIO(open(__file__.replace('.py', '.in')).read())

n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

d = [False] * (10 ** 6 + 1)
s = 0
for i in x:
    s += i
    d[s] = True

s = 0
c = 0
for i in y:
    s += i
    if d[s]:
        c += 1

print(c)
# print(d[:100])
