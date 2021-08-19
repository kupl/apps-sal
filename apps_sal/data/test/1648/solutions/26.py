import sys
input = sys.stdin.readline
(N, K) = (int(x) for x in input().rstrip('\n').split())
red = 1
blue = 1
res = 1
sub = N - K + 1
for i in range(1, K + 1):
    red = red * (N - K + 2 - i) // i
    if i == 1:
        blue = 1
    else:
        blue = blue * (K + 1 - i) // (i - 1)
    res = red * blue
    print(res % 1000000007)
