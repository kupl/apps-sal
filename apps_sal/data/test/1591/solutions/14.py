(n, k) = map(int, input().split())
d = [0] * (k + 1)
for i in range(n):
    a = int(input())
    d[a] += 1
d.sort(reverse=True)
count = 0
for i in range(k):
    count += d[i] - d[i] % 2
    d[i] = d[i] % 2
d.append(1)
count += d.count(1) // 2
print(count)
