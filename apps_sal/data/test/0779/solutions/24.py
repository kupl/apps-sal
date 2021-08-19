#import sys
#from io import StringIO
#sys.stdin = StringIO(open(__file__.replace('.py', '.in')).read())

n = int(input())

c = 0
for i in range(1, n):
    if (n - i) % i == 0:
        c += 1
print(c)
