n = int(input())
b = list(map(int, input().split()))
count = b[0] + b[-1]
for i in range(n - 2):
    count += min(b[i], b[i + 1])
print(count)
