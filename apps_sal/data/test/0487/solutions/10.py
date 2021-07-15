n = int(input())
a = list(map(int, input().split()))

k = max(a)
s = sum(a)

while s >= k * n - s:
    k += 1

print(k)

