n, k = map(int, input().split())
a = list(map(int, input().split()))
i = 0
s = sum(a)
while (s + i * k) / (n + i) < k - 0.5:
    i += 1
print(i)
