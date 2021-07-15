n = int(input())
a = sorted(int(x) for x in input().split())
m = int(input())
b = sorted(int(x) for x in input().split())
i, j, val = 0, 0, 0
while i < n and j < m:
    if a[i] < b[j] - 1:
        i += 1
    elif b[j] < a[i] - 1:
        j += 1
    else:
        i += 1
        j += 1
        val += 1
print(val)
