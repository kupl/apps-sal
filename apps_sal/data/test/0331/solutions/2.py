n, m, k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = []
for i in range(len(a)):
    if a[i] != 0 and a[i] <= k:
        b.append(abs(i + 1 - m))
print(min(b) * 10)


