n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

print(sum(min(x.count(1), x.count(2)) for x in (a[i::k] for i in range(k))))

