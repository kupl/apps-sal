n = int(input())
a = list(map(int, input().split()))
cur = 15
for i in range(n):
    if a[i] > cur:
        break
    cur = a[i] + 15
cur = min(cur, 90)
print(cur)

