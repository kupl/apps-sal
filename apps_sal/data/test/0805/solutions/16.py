bot = True
n = int(input())

d = [1] * 100

a, b = list(map(int, input().split()))

for _ in range(n - 1):

    l, r = list(map(int, input().split()))

    for i in range(l, r):

        d[i] = 0

print(sum(d[a:b]))
