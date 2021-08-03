n = int(input())
h = list(map(int, input().split()))
a = 0
count = 0
for i in range(n):
    if h[i] >= a:
        a = h[i]
        count += 1

print(count)
