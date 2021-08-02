n, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))
print(sum((lambda x: min(x - n // k, 2 * n // k - x))(sum(a[i::k])) for i in range(k)))
