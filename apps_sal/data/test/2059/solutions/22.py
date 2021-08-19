def R():
    return map(int, input().split())


n = int(input())
k = 10 ** 9
a = list(R())
for i in range(n):
    k = min(k, a[i] / max(i, n - 1 - i))
print(int(k))
