n = int(input())
b = list(map(int, input().split()))
b.insert(0, 10000000.0)
b.append(10000000.0)
count = 0
for i in range(n):
    count += min(b[i], b[i + 1])
print(count)
