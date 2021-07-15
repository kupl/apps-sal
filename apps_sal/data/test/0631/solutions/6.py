import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    if m==sum(a):
        print("YES")
    else:
        print("NO")

