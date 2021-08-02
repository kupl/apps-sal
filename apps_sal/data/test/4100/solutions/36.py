n, k, q = map(int, input().split())
Points = [k - q] * n

for i in range(q):
    a = int(input()) - 1
    Points[a] += 1

for p in Points:
    if p > 0:
        print('Yes')
    else:
        print('No')
