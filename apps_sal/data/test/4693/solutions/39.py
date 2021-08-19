import sys
input = sys.stdin.readline
(a, b) = list(map(int, input().split()))
ab = a + b
if ab >= 10:
    print('error')
else:
    print(ab)
