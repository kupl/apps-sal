n = int(input())

a = list(map(int, input().split()))

ma = [1] * n

for i in range(1, n):

    ma[i] = max(ma[i - 1], a[i] + 1)

for i in range(n - 2, -1, -1):

    ma[i] = max(ma[i + 1] - 1, ma[i])

print(sum(ma) - sum(a) - n)


# Made By Mostafa_Khaled
