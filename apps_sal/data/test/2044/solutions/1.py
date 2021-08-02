'''input
1 100
99
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for d in range(n):
    c += a[d]
    print(c // m, end=' ')
    c %= m
