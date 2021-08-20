n = int(input())
a = [0] * n
for (i, x) in enumerate(map(int, input().split())):
    a[x - 1] = i
print(sum((abs(a[i + 1] - a[i]) for i in range(n - 1))))
