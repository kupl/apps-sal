(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
poc = 0
for i in range(k):
    (p1, p2) = (0, 0)
    for j in range(i, n, k):
        if a[j] == 1:
            p1 += 1
        else:
            p2 += 1
    poc += min(p1, p2)
print(poc)
