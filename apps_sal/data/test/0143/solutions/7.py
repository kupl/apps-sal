n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = n + 1

i = 0
j = 1

while i < n:
    if a[i] >= j:
        i += 1
        j += 1
    else:
        while i < n and a[i] < j:
            i += 1
        if i != n:
            j += 1
            i += 1

print(j)

