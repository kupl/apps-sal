(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if a[i] <= k:
        c += 1
    else:
        break
for i in range(len(a) - 1, -1, -1):
    if a[i] <= k:
        c += 1
    else:
        break
print(min(c, len(a)))
