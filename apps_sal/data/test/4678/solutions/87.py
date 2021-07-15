n = int(input())
a = [int(i) for i in input().split()]

ans = 0
max_a = a[0]

for i in range(1, n):
    if max_a > a[i]:
        ans += max_a - a[i]
    elif max_a == a[i]:
        pass
    else:
        max_a = a[i]
print(ans)
