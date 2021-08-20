(n, t) = map(int, input().split())
l = list(map(int, input().split()))
total = 0
for i in range(n):
    if i == n - 1:
        total += t
        break
    if l[i + 1] - l[i] >= t:
        total += t
    else:
        total += l[i + 1] - l[i]
print(total)
