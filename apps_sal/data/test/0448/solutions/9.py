n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [[a[i] // m + (a[i] % m != 0), i] for i in range(n)]
b = sorted(b)
print(b[-1][1] + 1)
