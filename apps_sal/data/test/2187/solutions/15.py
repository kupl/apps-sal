
from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    a = list(map(int,stdin.readline().split()))

    ans = 0
    for i in range(n-1):
        ans += max(0 , a[i] - a[i+1])
    print (ans)
