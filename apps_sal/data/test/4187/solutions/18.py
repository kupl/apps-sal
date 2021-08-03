n = int(input())
a = [int(i) for i in input().split()]
a.extend(a)
i, j = 0, 0
m = 0
while i < len(a):
    while j < len(a) and a[j] == 1:
        j += 1
    j += 1
    m = max(m, j - i - 1)
    i = j
print(m)
