def sq(x): return x * x


a = list(map(int, input().split()))
print(sq(a[0] + a[1] + a[2]) - sq(a[0]) - sq(a[2]) - sq(a[4]))
