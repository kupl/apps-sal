n, m = list(map(int, input().split()))
arr = []
for i in range(m):
    x, y = list(map(int, input().split()))
    arr.append(x)
    arr.append(y)

print(n - 1)
for i in range(1, n + 1):
    if (i in arr) == False:
        for j in range(1, n + 1):
            if i != j:
                print(str(i) + ' ' + str(j))
        break
