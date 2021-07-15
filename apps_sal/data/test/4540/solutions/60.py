n = int(input())
a = [0] + [int(x) for x in input().split()] + [0]
diff = [abs(a[i] - a[i + 1]) for i in range(n + 1)]
tot = sum(diff)
for i in range(1, n + 1):
    print(tot - diff[i - 1] - diff[i] + abs(a[i - 1] - a[i + 1]))
