n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(sum([(i + 1) * a[i] for i in range(n)]) + sum(a[:-1]))
