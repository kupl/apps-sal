n, s = list(map(int, input().split()))

big = s // n
r = s - big * n
if r > 0:
    print(big + 1)
else:
    print(big)
