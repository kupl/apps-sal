import sys
input = sys.stdin.readline
for k in range(int(input())):
    a, b, x, y = list(map(int, input().split(" ")))
    print(max(a*y, b*x, (b-1-y)*a, (a-1-x)*b)) 

