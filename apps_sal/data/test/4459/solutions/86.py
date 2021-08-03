n = int(input())
a = list(map(int, input().split()))

values = {}
cnt = n

for i in range(n):
    if a[i] in values:
        values[a[i]] += 1
    else:
        values[a[i]] = 1

    if values[a[i]] == a[i]:
        cnt -= a[i]

print(cnt)
