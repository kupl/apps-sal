n = int(input())
a = list(map(int, input().split()))
an = 0
for i in range(1, n - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1] or a[i] < a[i + 1] and a[i] < a[i - 1]:
        an += 1
print(an)

