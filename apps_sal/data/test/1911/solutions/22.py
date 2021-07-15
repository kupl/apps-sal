n, k = [int(item) for item in input().split()]
a = [int(item) for item in input().split()]
diff = []
for a1, a2 in zip(a[:], a[1:]):
    diff.append(a2 - a1)
diff.sort()
print(sum(diff) - sum(diff[::-1][:k-1]))
