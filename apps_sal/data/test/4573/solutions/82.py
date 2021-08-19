n = int(input())
X = list(map(int, input().split()))
sorted_x = sorted(X)
(l, r) = (sorted_x[n // 2 - 1], sorted_x[n // 2])
for x in X:
    if x < r:
        print(r)
    else:
        print(l)
