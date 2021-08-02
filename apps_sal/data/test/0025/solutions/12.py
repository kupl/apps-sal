
s = input()
n = int(s.split(' ')[0])
k = int(s.split(' ')[1])

arr = []
for i in range(n):
    arr.append([0] * n)
if k > n * n:
    print(-1)
else:
    l = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                if l < k:
                    if i == j:
                        arr[i][j] = 1
                        l += 1
                    elif l < k - 1:
                        arr[i][j] = 1
                        arr[j][i] = 1
                        l += 2

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
