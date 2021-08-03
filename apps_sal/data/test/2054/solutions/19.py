import sys
input = sys.stdin.readline
for f in range(int(input())):
    a, b = list(map(int, input().split()))
    print(min((a + b) // 3, a, b))
