
k, n = map(int, input().split())
a = list(map(int, input().split()))

c = a[0]
a.append(c + k)
b = [a[i + 1] - a[i] for i in range(n)]

print(k - max(b))
