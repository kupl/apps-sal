n = int(input())
h = [int(i) for i in input().split()]
count = 1
for i in range(1, n):
    if h[i] >= max(h[:i]):
        count += 1
print(count)
