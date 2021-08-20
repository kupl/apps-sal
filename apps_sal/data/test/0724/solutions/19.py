(q, w) = map(int, input().split())
a = list(map(int, input().split()))
s = [0 for i in range(0, q)]
a.sort()
for i in range(0, q - 1):
    j = i + 1
    while a[j] - a[i] <= w:
        s[i] += 1
        j += 1
        if j == q:
            break
print(q - max(s) - 1)
