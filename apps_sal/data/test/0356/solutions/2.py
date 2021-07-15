n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
if sum(a) != sum(b):
    print(-1)
    return
i = 0
j = 0
while i < n and j < m:
    while a[i] != b[j] and i < n and j < m:
        if i < n - 1 and a[i] < b[j]:
            a[i + 1] += a[i]
            a[i] = -1
            i += 1
        elif j < m - 1:
            b[j + 1] += b[j]
            b[j] = -1
            j += 1
    if a[i] == b[j]:
        i += 1
        j += 1
    else:
        print(-1)
        return
ans = 0
for i in a:
    if i != -1:
        ans += 1
print(ans)

    

