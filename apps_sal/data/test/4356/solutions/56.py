n, m = map(int, input().split())
a = [input() for i in range(n)]
b = [input() for j in range(m)]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        for k in range(m):
            if a[k + i][0 + j:m + j] != b[k]:
                break
        else:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")
