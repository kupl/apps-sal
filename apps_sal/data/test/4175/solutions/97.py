n = int(input())
w = [input() for i in range(n)]
check = True
for i in range(1, n):
    for j in range(i):
        if w[i] == w[j]:
            check = False
    if w[i - 1][-1] != w[i][0]:
        check = False
print("Yes" if check else "No")
