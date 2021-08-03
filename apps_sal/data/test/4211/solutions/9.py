n = int(input())
b = list(map(int, input().split()))
b.insert(0, 1e7)
b.append(1e7)
count = 0
for i in range(n):
    count += min(b[i], b[i + 1])
print(count)
