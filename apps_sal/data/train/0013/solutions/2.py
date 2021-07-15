# import sys
#
# input = lambda: sys.stdin.readline().strip()
for i in range(int(input())):
    n,g, b = list(map(int, input().split()))
    n1 = n
    n = (n+1)//2
    k = n//g
    if n%g:
        print(max(n1,k*(g+b)+n%g))
    else:
        print(max(n1,g*k+b*(k-1)))

