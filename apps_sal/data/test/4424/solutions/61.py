import sys
input = sys.stdin.readline

k, x = map(int, input().split())
if k * 500 >= x:
    print("Yes")
else:
    print("No")
