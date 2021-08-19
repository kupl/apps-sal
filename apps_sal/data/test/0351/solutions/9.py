(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
result = 0
for d in a:
    while d > 2 * k:
        k *= 2
        result += 1
    k = max(d, k)
print(result)
