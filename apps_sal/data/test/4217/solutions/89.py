(n, m) = list(map(int, input().split()))
l = [0] * (m + 1)
count = 0
for i in range(n):
    k = list(map(int, input().split()))
    for j in range(1, k[0] + 1):
        l[k[j]] += 1
for i in range(1, m + 1):
    if l[i] == n:
        count += 1
print(count)
