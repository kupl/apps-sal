import sys
input = sys.stdin.readline
X = int(input())
A = int(input())
B = int(input())
X -= A
print(X - X // B * B)
