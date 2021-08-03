n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

if n < sum(a):
    print((-1))
else:
    print((n - sum(a)))
