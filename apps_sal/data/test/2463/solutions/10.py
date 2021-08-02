n = int(input())
print((n - 1) // 2)
a = [int(i) for i in input().split(" ")]
a.sort()
b = []
for i in range(n):
    if i % 2 == 0:
        b.append(a[n // 2 + i // 2])
    else:
        b.append(a[i // 2])
print(" ".join([str(i) for i in b]))
