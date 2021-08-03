n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
k = 0
for i in range(n):
    for j in range(n):
        if i != j and a[i][0] == a[j][1]:
            k += 1
            break

print(n - k)
