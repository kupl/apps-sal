n, m = map(int, input().split())
a = ["" for _ in range(n)]
b = ["" for _ in range(m)]
for i in range(n):
    ai = str(input())
    a[i] = ai
for i in range(m):
    bi = str(input())
    b[i] = bi
for i in range(n - m + 1):
    for j in range(n - m + 1):
        flag = False
        for k in range(m):
            for l in range(m):
                if a[i + k][j + l] != b[k][l]:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            print("Yes")
            return
print("No")
