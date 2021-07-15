n = int(input())
a = [int(x) for x in input().strip().split(' ')]
m = min(a)

i = [x for x in range(n) if a[x] == m]

d = [i[x + 1] - i[x] for x in range(len(i) - 1)]
print(min(d))

