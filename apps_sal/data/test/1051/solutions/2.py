import sys
input = sys.stdin.readline
k = int(input())
large = max(map(int, input().split()))
print(max(0, large - 25))
