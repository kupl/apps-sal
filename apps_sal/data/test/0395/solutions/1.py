a = list(map(int, input().split()))
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            if a[i] + a[j] + a[k] == sum(a) - a[i] - a[j] - a[k]:
                print("YES")
                return
print("NO")
