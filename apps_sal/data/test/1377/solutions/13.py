n = int(input())
a = list(map(int, input().split()))
i = a.index(max(a))
f = True
j = i + 1
while j < n:
    if a[j] >= a[j - 1]:
        f = False
    j += 1
j = i - 1
while j >= 0:
    if a[j] >= a[j + 1]:
        f = False
    j -= 1
print('YES' if f else 'NO')
