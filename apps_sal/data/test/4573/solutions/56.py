import bisect

n = int(input())
X = list(map(int, input().split()))

sorted_x = sorted(X)

l, r = sorted_x[n // 2], sorted_x[n // 2 - 1]

for x in X:
    if bisect.bisect_left(sorted_x, x) < n // 2:
        print(l)
    else:
        print(r)
