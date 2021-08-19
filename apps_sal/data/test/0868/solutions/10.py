# cf383 yl 1
n = int(input())
# l=list(map(int,input().split()))
if n == 0:
    print(1)
else:
    print([6, 8, 4, 2, 6, 8, 4][n % 4])
