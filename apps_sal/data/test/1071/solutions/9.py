from math import ceil
k = sum(map(int, input().split()))
m = sum(map(int, input().split()))
p = int(input())

k = ceil(k / 5.)
m = ceil(m / 10.)

if p - m - k >= 0:
    print("YES")
else:
    print("NO")
