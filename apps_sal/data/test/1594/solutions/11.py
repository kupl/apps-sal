n, m = list(map(int, input().split()))
A = []
for i in range(n):
    c, t = list(map(int, input().split()))
    A.append(c * t)
i = p = 0
for v in [int(x) for x in input().split()]:
    while(p < v): p, i = p + A[i], i + 1
    print(i)
