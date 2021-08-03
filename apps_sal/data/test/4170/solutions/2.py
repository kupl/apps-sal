n = int(input())
h = tuple(map(int, input().split()))
count = [0] * n
h = h[::-1]
for i in range(1, n):
    count[i] = count[i - 1] + 1 if h[i] >= h[i - 1] else 0
print(max(count))
