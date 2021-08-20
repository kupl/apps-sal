n = int(input())
w = [int(x) for x in input().split()]
for i in range(int(input())):
    (x, y) = (int(x) for x in input().split())
    if x > 1:
        w[x - 2] += y - 1
    if x < n:
        w[x] += w[x - 1] - y
    w[x - 1] = 0
for b in w:
    print(b)
