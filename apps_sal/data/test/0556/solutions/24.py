
from sys import stdin, stdout
input = stdin.readline

l, r, k = list(map(int, input().split()))
res = []
n = 1
while n <= r:
    if n >= l:
        res.append(str(n))

    n *= k
if len(res):
    stdout.write(" ".join(res))
else:
    stdout.write("-1"
                 )
