import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

if sum(A) % 2 == 0 and max(A) <= sum(A) - max(A):
    print("YES")
else:
    print("NO")
