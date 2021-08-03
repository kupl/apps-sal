n, a, b, c, t = list(map(int, input().split()))
l = [int(i) for i in input().split()]
if b >= c:
    print(n * a)
else:
    print(sum([a + (t - j) * (c - b) for j in l]))
