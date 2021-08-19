n = int(input())
d = list(map(int, input().split()))
a = [0]
a.extend(d)
an = 0
for i in range(n + 1):
    if a[i] > a[i - 1]:
        an += (a[i] - a[i - 1]) * (n - a[i] + 1)
    if a[i] < a[i - 1]:
        an += (a[i]) * (a[i - 1] - a[i])
# print(an)
print(an)
