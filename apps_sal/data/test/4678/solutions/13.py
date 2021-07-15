n = int(input())
a = list(map(int, input().split()))
max = a[0]
ans = 0

for i in range(1, n):
    if max < a[i]:
        max = a[i]

    if a[i] < max:
        ans += max - a[i]

print(ans)
