n, m = list(map(int, input().split()))

a = list(map(int, input().split()))

c = 0

ans = -1

for i in range(n - 1):

    while c < n - 1 and a[c + 1] - a[i] <= m:

        c += 1

    if i < c - 1:

        ans = max(ans, (a[c] - a[i + 1]) / (a[c] - a[i]))

print(ans)


# Made By Mostafa_Khaled
